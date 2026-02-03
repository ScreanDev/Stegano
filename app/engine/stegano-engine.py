from PIL import Image
from pathlib import Path

class SteganoEngine:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.pixels = self.image.load()
        self.width, self.height = self.image.size
        self.title = self.image.filename.split("/")[-1].split(".")[0] + "_stegano.png"

        # Create a new image with RGB mode and black background
        self.final_img = Image.new('RGB', (self.width, self.height), color='black')

    def encode_message(self, message):

        # We add this marker at the end to indicate the end of the message
        message += str("\x00")
        # Convert each character from the provided message to its ASCII code,
        # then for each, that ASCII code to 8-bit binary.
        binary_message = ''.join(format(ord(char), '08b') for char in message)

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
        for i in range(0, len(binary_retrans), 8):
            # Convert each 8-bit segment to its corresponding character
            char_to_add = chr(int(binary_retrans[i:i+8], 2))
            # Stop if we reach the end marker
            if char_to_add == '\x00':
                break
            ascii_retrans += char_to_add

        return ascii_retrans