from pathlib import Path
import sys
from tkinter.messagebox import askyesno, showwarning, showinfo, showerror
from tkinter.ttk import Button
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))
from app.engine.stegano_engine import SteganoEngine
from app.events.call_window import call_app_window, call_encode_window

def encode_process(img_path, message):
    try:
        ste = SteganoEngine(img_path)
        encoded_img = ste.encode_message(message)
        encoded_img.show()

        save_path = str(Path.home() / "Downloads" / ste.title)
        encoded_img.save(save_path, format="png")
        alert_img_saved(save_path)
    except Exception as e:
        alert_error(str(e))


def decode_process(img_path):
    ste = SteganoEngine(img_path)
    image = ste.image
    decoded_message = ste.decode_message(image)
    print("Decoded message:", decoded_message)


def alert_img_saved(save_path):
    showinfo('Success', f'Image successfully saved in folder: {Path(save_path).parent} as {Path(save_path).name}')

def alert_error(error_message):
    showerror('An error occurred', f'An error occurred when trying to encode the image: {error_message}')

if __name__ == "__main__":
    call_app_window()