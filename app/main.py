from pathlib import Path
import sys
from tkinter import Image
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))
from app.engine.stegano_engine import SteganoEngine


print("------------------ STEGANO ENGINE TEST ------------------")
img_path = input("Type a path to an image file to use it for encoding/decoding: ")

try:
    ste = SteganoEngine(img_path)
    final_img = ste.encode_message("Wisdom is here to check what you're dealing with. Gotcha.")

    final_img.show()

    downloads_path = str(Path.home() / "Downloads" / ste.title)
    final_img.save(downloads_path, format="png")

    decoded_message = ste.decode_message(final_img)
    print(decoded_message)
except Exception as e:
    print(f"An error occurred: {e}")