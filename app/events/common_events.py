import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


def load_encoding_ui(frame, file_path):
    """
    Load the encoding UI preview in the given frame with the selected image file.
    
    :param frame: The frame widget where the encoding UI preview will be loaded.
    :param file_path: The path to the image file to be previewed.
    """
    if file_path:
        # Clear previous preview if exists
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


def load_decoding_img_preview(frame, file_path):
    """
    Load the decoding image preview in the given frame with the selected image file.
    
    :param frame: The frame widget where the decoding image preview will be loaded.
    :param file_path: The path to the image file to be previewed.
    """
    if file_path:
        # Clear previous preview if exists
        for widget in frame.winfo_children():
            if hasattr(widget, 'is_preview') and widget.is_preview:
                widget.destroy()

        loaded_img_label = Label(frame, text=f"Selected file: {os.path.basename(file_path)}", bg="#f0f0f0", wraplength=200, justify=CENTER)
        loaded_img_label.pack()
        loaded_img_label.is_preview = True

        preview_frame = Frame(frame, bg="white", bd=1, relief="solid")
        preview_frame.pack()
        preview_frame.is_preview = True

        pil_image = Image.open(file_path)
        pil_image.thumbnail((200, 140))
        tk_image = ImageTk.PhotoImage(pil_image)
        img_label = Label(preview_frame, image=tk_image, bg="white")
        img_label.image = tk_image  # Keep a reference to avoid garbage collection
        img_label.pack()

        decode_ready_frame = Frame(frame, bg="#f0f0f0", bd=2, borderwidth=1, relief="flat")
        decode_ready_frame.pack(side=TOP, fill=X)
        decode_ready_frame.is_preview = True

        decode_button = Button(frame, text="Decode Image", bg="white")
        decode_button.pack(pady=10)
        decode_button.is_preview = True
        decode_button.is_decode_button = True


def select_file_in_explorer(file_formats=None):
    """
    Open a file dialog for the user to select a file.
    
    :param file_formats: A tuple containing the file type description and the file extension pattern, e.g., ("Images", "*.png *.jpg").
                         If None, defaults to all files.
    """
    root = Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[file_formats] if not file_formats is None else [("All Files", "*.*")]
    )
    return file_path

# Utility function to update decoded message textbox, preventing user's edits
def update_decoded_msg_textbox(textbox, message):
    """
    Update the content of a textbox widget with a given message.
    Temporarily enables the textbox to allow editing, then disables it to prevent user modifications.
    
    :param textbox: The Text widget to update.
    :param message: The string message to insert into the textbox.
    """
    textbox.config(state=NORMAL)
    textbox.delete(1.0, END)
    textbox.insert("1.0", message)
    textbox.config(state=DISABLED)