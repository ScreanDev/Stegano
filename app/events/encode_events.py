import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


def load_encoding_ui(frame, file_path):
    for widget in frame.winfo_children():
        if hasattr(widget, 'is_preview') and widget.is_preview:
            widget.destroy()

    loaded_img_label = Label(frame, text=f"Selected file: {os.path.basename(file_path)}", bg="#f0f0f0", wraplength=200, justify=CENTER)
    loaded_img_label.pack(pady=10)
    loaded_img_label.is_preview = True

    preview_frame = Frame(frame, bg="white", bd=1, relief="solid")
    preview_frame.pack(pady=10)
    preview_frame.is_preview = True

    pil_image = Image.open(file_path)
    pil_image.thumbnail((200, 140))
    tk_image = ImageTk.PhotoImage(pil_image)
    img_label = Label(preview_frame, image=tk_image, bg="white")
    img_label.image = tk_image  # Keep a reference to avoid garbage collection
    img_label.pack()



def select_file_in_explorer(file_formats=None):
    root = Tk()
    root.withdraw()
    start = os.path.abspath("assets")
    
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[file_formats] if not file_formats is None else [("All Files", "*.*")]
    )
    return file_path