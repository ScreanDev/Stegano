from PIL import Image

class SteganoEngine:
    """
    A class that provides methods to encode and decode messages within images using steganography techniques.
    The encoding process modifies the least significant bit (LSB) of the red channel of each pixel to embed the binary representation of the message.
    The decoding process retrieves the LSBs to reconstruct the original message.
    """
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.pixels = self.image.load()
        self.width, self.height = self.image.size
        self.title = self.image.filename.split("/")[-1].split(".")[0] + "_stegano.png"

        self.signature = "STEGANO"
        self.signature_binary_size = len(''.join(format(ord(char), '08b') for char in self.signature))

        self.message_size_counter_length = 5

        # Create a new image with RGB mode and black background
        self.final_img = Image.new('RGB', (self.width, self.height), color='black')

    def encode_message(self, message, is_script=False):
        """
        Encode a message into the image by modifying the least significant bit of the red channel of each pixel.
        The process converts each character from the provided message to its ASCII code,
        then for each, that ASCII code to 8-bit binary.
        
        :param self: The instance of the SteganoEngine class.
        :param message: The message string to encode into the image.
        """
        
        # We also add a signature at the beginning of the message to check if the image was encoded with this tool when decoding
        binary_message = ''.join(format(ord(char), '08b') for char in self.signature)

        # Then we add a bit right after the signature to mark if the message is a Python script or not
        if is_script:
            binary_message += ''.join(format(ord("1"), '08b'))
        else:
            binary_message += ''.join(format(ord("0"), '08b'))

        # We also add the size of the message (in number of characters) as a 5-character string right after the signature
        # This will be the stop condition when decoding characters from the binary string
        message_size = str(len(self.signature) + 1 + self.message_size_counter_length + len(message)).zfill(self.message_size_counter_length)
        binary_message += ''.join(format(ord(char), '08b') for char in message_size)

        # Now we can add the actual message
        binary_message += ''.join(format(ord(char), '08b') for char in message)

        # This counter will check the n-th character from the binary message.
        string_elt_counter = 0
        for px in range(self.width):
            for py in range(self.height):
                # Get the RGB tuple for the pixel at coords px:py
                rgb_code = self.pixels[px, py]
                # O means the current pixel's red channel is an even number, 1 if odd
                # If the current value is incorrect we change it (making the red channel's value even or odd)
                # This is the way we'll encode the binary message in our image
                if (rgb_code[0] % 2 == 0 and binary_message[string_elt_counter] == '1') or (rgb_code[0] % 2 != 0 and binary_message[string_elt_counter] == '0'):
                    # Ensure we'll not get out of bounds (value can't exceed 255)
                    if rgb_code[0] < 255:
                        rgb_code = (rgb_code[0] + 1, rgb_code[1], rgb_code[2])
                    else:
                        rgb_code = (rgb_code[0] - 1, rgb_code[1], rgb_code[2])
                
                
                # Print the new pixel color to our final image
                self.final_img.putpixel((px, py), rgb_code)

                if len(binary_message) - 1 > string_elt_counter:
                    string_elt_counter += 1
        
        return self.final_img
    
    
    def decode_message(self, image):
        """
        Decode a message from the provided image by retrieving the least significant bit of the red channel of each pixel.
        The process reconstructs the binary string from the LSBs, then converts it back to ASCII characters to retrieve the original message.
        
        :param self: The instance of the SteganoEngine class.
        :param image: The image object from which to decode the message.
        """

        has_stegano_signature = False
        is_script = False

        try:
            # Get the pixel data from the provided image
            pixels = image.load()
            binary_retrans = ""

            for px in range(self.width):
                for py in range(self.height):
                    rgb_code = pixels[px, py]
                    # The opposite process of encoding: we get the LSB of the red channel
                    binary_retrans += str(rgb_code[0] % 2)

            # Now we need to convert the binary string back to ASCII
            ascii_retrans = ''
            
            has_stegano_signature = self.has_signature(binary_retrans)

            if has_stegano_signature:
                binary_retrans = binary_retrans[self.signature_binary_size:]
                # After the signature, we have a bit to check if the message is a Python script or not
                is_script = self.is_script(binary_retrans)
                binary_retrans = binary_retrans[8:]
            
            message_size = self.get_message_size(binary_retrans)
            binary_retrans = binary_retrans[self.message_size_counter_length * 8:(message_size * 8) - 8 - self.signature_binary_size if has_stegano_signature else 0]

            for i in range(0, len(binary_retrans), 8):
                # Convert each 8-bit segment to its corresponding character
                char_to_add = chr(int(binary_retrans[i:i+8], 2))
                ascii_retrans += char_to_add

            return ascii_retrans, has_stegano_signature, is_script
        except Exception as e:
            if has_stegano_signature:
                raise Exception(f"An error occurred during decoding: {str(e)}")
            else:
                raise Exception(f"No Stegano signature was detected, so the image might not have been encoded with this tool or might not contain any hidden message.\n\nAn error occurred during decoding: {str(e)}.")


    def has_signature(self, binary_message):
        """
        Check if the binary message starts with the expected signature to determine if the image was likely encoded with this tool.
        
        :param self: The instance of the SteganoEngine class.
        :param binary_message: The binary string extracted from the image to check for the signature.
        """
        # Extract the beginning of the binary message to check for the signature
        extracted_signature_binary = binary_message[:self.signature_binary_size]
        extracted_signature = ''
        for i in range(0, len(extracted_signature_binary), 8):
            extracted_signature += chr(int(extracted_signature_binary[i:i+8], 2))
        return extracted_signature == self.signature
    
    def get_message_size(self, extracted_binary_message):
        """
        Get the size of the hidden message from the extracted binary string.
        
        :param self: The instance of the SteganoEngine class.
        :param extracted_binary_message: The binary string from the image whose signature & script bit are extracted containing the message size.
        """
        # Extract the message size from the binary message
        end_index = self.message_size_counter_length * 8
        message_size_binary = extracted_binary_message[:end_index]
        message_size = ''
        for i in range(0, len(message_size_binary), 8):
            message_size += chr(int(message_size_binary[i:i+8], 2))
        return int(message_size)
    

    def is_script(self, extracted_binary_message):
        """
        Check if the message is marked as a Python script by looking at the bit right after the signature in the binary message.
        
        :param self: The instance of the SteganoEngine class.
        :param extracted_binary_message: The binary string from the image whose signature is extracted containing the script bit.
        """
        # Extract the bit right after the signature to check if it's a Python script or not
        script_bit_binary = chr(int(extracted_binary_message[:8], 2))
        return script_bit_binary == str(1)