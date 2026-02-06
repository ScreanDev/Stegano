import os
import sys
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


def load_encoding_ui(frame, file_path, encode_ready_frame):
    """
    Load the encoding UI preview in the given frame with the selected image file.
    
    :param frame: The frame widget where the encoding UI preview will be loaded.
    :param file_path: The path to the image file to be previewed.
    :param encode_ready_frame: The frame widget for the "ready to encode" section.
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

        encode_ready_frame.pack(side=BOTTOM, fill=X)


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


def hide_export_container(load_export_frame, load_exec_button):
    """
    Hide the export options frame from the decoding UI and the create executable button.
    
    :param load_export_frame: The frame widget containing the export options to be hidden.
    :param load_exec_button: The button widget for creating an executable to be hidden.
    """
    load_export_frame.pack_forget()
    load_exec_button.pack_forget()


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


def copy_to_clipboard(text):
    """
    Copy the given text to the system clipboard.
    
    :param text: The string text to be copied to the clipboard.
    """
    root = Tk()
    root.withdraw()  # Hide the root window
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(text)  # Append the text to the clipboard
    root.update()  # Update the clipboard
    root.destroy()  # Destroy the root window

def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller
    
    :param relative_path: The relative path to the resource file.
    :return: The absolute path to the resource file.
    """
    if getattr(sys, 'frozen', False):
        # We are running the compiled executable.
        # sys.executable points to the .exe path
        base_path = os.path.dirname(sys.executable)
    else:
        # We are in a normal Python environment,
        # so we can use the current file's directory as the base path
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)