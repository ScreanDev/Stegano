from pathlib import Path
import sys
from tkinter.messagebox import showinfo, showerror
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))
from app.engine.stegano_engine import SteganoEngine
from app.events.call_window import call_app_window
from app.events.common_events import update_decoded_msg_textbox


# ----------------------
# ENCODE FUNCTION
# ----------------------
def encode_process(img_path, message):
    """
    Uses the SteganoEngine to encode the message within the specified image file,
    then shows the resulting image and saves it in the user's Downloads folder.
    
    :param img_path: The path to the image file to encode.
    :param message: The message to encode within the image.
    """
    try:
        # Use the SteganoEngine to encode the message within the image
        ste = SteganoEngine(img_path)
        encoded_img = ste.encode_message(message)
        encoded_img.show()

        # Save the encoded image
        save_path = str(Path.home() / "Downloads" / ste.title)
        encoded_img.save(save_path, format="png")
        alert_img_saved(save_path)
    except Exception as e:
        alert_encoding_error(str(e))


# ----------------------
# DECODE FUNCTION
# ----------------------
def decode_process(img_path, output_textbox = None, description_label = None):
    """
    Uses the SteganoEngine to decode the message within the specified image file,
    then updates the output_textbox and description_label if provided.
    
    :param img_path: The path to the image file to decode.
    :param output_textbox: The Text widget to update with the decoded message. If None, the decoded message will be printed in the console.
    :param description_label: The Label widget to update with the decoding status. If None, the status will be printed in the console.
    """
    try:
        # Use the SteganoEngine to try decoding a message within the image
        ste = SteganoEngine(img_path)
        image = ste.image

        # Return a tuple with the decoded message and a boolean indicating if the stegano signature was detected
        decoded_message, has_stegano_signature = ste.decode_message(image)
        
        # If the stegano signature was detected, we can be more confident in the decoding result, so we display a success message.
        # Otherwise, we warn the user that the image might not have been encoded with this tool or might not contain any hidden message,
        # but we still display the decoding result anyway.
        if has_stegano_signature:
            # We may not use a description label if debugging in the console
            if not description_label is None:
                description_label.config(text="Stegano signature detected! The image was encoded with this tool.", fg="#1d8138")
            else:
                # \033[33m is used to print in yellow color in the console
                print('\033[33m' + 'Stegano signature detected! The image was encoded with this tool.' + '\033[0m')
        else:
            # If not detected, we still try decoding.
            if not description_label is None:
                description_label.config(text="No Stegano signature detected. Continuing anyway.", fg="#b36b00")
            else:
                print('\033[33m' + 'No Stegano signature detected. Continuing anyway.' + '\033[0m')

        # Update the output textbox with the decoded message if provided, otherwise print it in the console
        if not output_textbox is None and not description_label is None:
            update_decoded_msg_textbox(output_textbox, decoded_message)
        else:
            print('\033[33m' + 'Decoded message:\n' + '\033[33m' + decoded_message + '\033[0m')

    except Exception as e:
        if not description_label is None:
            description_label.config(text=str(e), fg="red")
        else:
            print('\033[31m' + f'{str(e)}' + '\033[0m')



# ----------------------
# ALERTS
# ----------------------
def alert_img_saved(save_path):
    """Shows a success alert when the image is successfully saved after encoding."""
    showinfo('Success', f'Image successfully saved in folder: {Path(save_path).parent} as {Path(save_path).name}')

def alert_encoding_error(error_message):
    """Shows an error alert when an error occurs during the encoding process."""
    showerror('An error occurred', f'An error occurred when trying to encode the image: {error_message}')

def alert_decoding_error(error_message):
    """Shows an error alert when an error occurs during the decoding process."""
    showerror('An error occurred', f'An error occurred when trying to decode the image: {error_message}')


# ----------------------
# CORE APPLICATION WINDOW CALL
# ----------------------
if __name__ == "__main__":
    call_app_window()