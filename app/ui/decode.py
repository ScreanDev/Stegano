# coding: utf-8

from pathlib import Path
import sys
from tkinter import *
from fonts_properties import *

path_root = Path(__file__).parents[2]
sys.path.insert(0, str(path_root))
from app.events.common_events import load_decoding_img_preview, select_file_in_explorer, update_decoded_msg_textbox
from app.main import decode_process

file_path = ""

# ----------------------
# MAIN WINDOW SETUP
# ----------------------
decode_root = Tk()
decode_root.title("Decode an image")
decode_root.geometry("800x500")
decode_root.resizable(False, False)

# ----------------------
# MINIMAL EVENT FUNCTIONS
# ----------------------

def img_selection_event():
    """
    Handle the event when the user clicks the "Browse..." button to select an image file for decoding.
    Once selected, load the preview UI.
    """
    global file_path
    previous_file_path = file_path # Store the previous file path to check if the user cancelled the file selection dialog
    file_path = select_file_in_explorer(file_formats=("Images", "*.png"))

    if not (file_path == None or file_path == ""):
        # UI loading
        load_decoding_img_preview(img_select_frame, file_path)
        
        for widget in img_select_frame.winfo_children():
            if hasattr(widget, 'is_decode_button') and widget.is_decode_button:
                # Specifying properties we could not set when creating the button from common_events.py
                widget.config(font=button_text, command=lambda: decode_process(img_path=file_path, output_textbox=msg_content_textbox, description_label=decode_placeholder_label))
        update_decoded_msg_textbox(msg_content_textbox, "")
        decode_placeholder_label.config(text="The result of the decoding process will be displayed here.", fg="black")
    else:
        file_path = previous_file_path # If the user cancelled the dialog, keep the previous file path

# ----------------------
# ICONS / CANVAS LOADING
# ----------------------
encode_icon = PhotoImage(file="app/assets/ui/encode_icon.png")
decode_icon = PhotoImage(file="app/assets/ui/decode_icon.png")

# ----------------------
# TITLE SECTION
# ----------------------
header_frame = Frame(decode_root, bg="white", bd=0, relief="flat")
header_frame.pack(side=TOP, fill=X, pady=10)

header_title_container = Frame(header_frame, bg="white")
header_title_container.pack(expand=True)

decode_icon_canvas = Canvas(header_title_container, width=100, height=25, bd=0, bg="white", highlightthickness=0)
decode_icon_canvas.create_image(0, 0, anchor=NW, image=decode_icon)
decode_icon_canvas.pack(side=LEFT, pady=5)

title_header_label = Label(header_title_container, text="Decoding", bg="white", font=header_subtitle)
title_header_label.pack(side=LEFT, padx=10)

title_desc_label = Label(header_frame, text="Use this tool to decode messages hidden within image files. Extract and execute Python scripts embedded within the picture.", bg="white", font=desc_text, wraplength=750, justify=CENTER)
title_desc_label.pack(side=BOTTOM, pady=5)


# ----------------------
# BODY SECTION
# ----------------------
body_frame = Frame(decode_root, bg="#f0f0f0", bd=2, borderwidth=2, relief="flat")
body_frame.pack(fill=BOTH, pady=5, expand=True)


# ----------------------
# IMAGE SELECTION
# ----------------------
img_select_frame = Frame(body_frame, bg="#f0f0f0", bd=2, borderwidth=1, relief="solid")
img_select_frame.pack(side=LEFT, padx=10, fill=BOTH, expand=True)

img_title_container = Frame(img_select_frame, bg="#f0f0f0")
img_title_container.pack(side=TOP, padx=20, pady=5, fill=X)

img_title_label = Label(img_title_container, text="Select an image file to decode:", bg="#f0f0f0", font=smaller_body_text, wraplength=200, justify=LEFT)
img_title_label.pack(side=LEFT)

img_btn_container = Frame(img_select_frame, bg="#f0f0f0")
img_btn_container.pack(side=TOP, padx=20, pady=5, fill=X)

img_select_btn = Button(img_btn_container, text="Browse...", bg="white", font=button_text, command=lambda: img_selection_event())
img_select_btn.pack(side=LEFT)

img_decode_desc_container = Frame(img_select_frame, bg="#f0f0f0")
img_decode_desc_container.pack(side=TOP, padx=20, pady=5, fill=X)

img_decode_desc = Label(img_decode_desc_container, text="", bg="#f0f0f0", font=desc_text, wraplength=300, justify=LEFT)
img_decode_desc.pack(side=LEFT, pady=5)


# ----------------------
# DECODE MESSAGE SECTION
# ----------------------
decode_content_frame = Frame(body_frame, bg="#f0f0f0", bd=2, borderwidth=1, relief="solid")
decode_content_frame.pack(side=RIGHT, padx=10, fill=BOTH, expand=True)

decode_placeholder_label = Label(decode_content_frame, text="The result of the decoding process will be displayed here.", bg="#f0f0f0", fg="black", font=desc_text, wraplength=200, justify=CENTER)
decode_placeholder_label.pack(pady=20)

msg_content_container = Frame(decode_content_frame, bg="#ffffff")
msg_content_container.pack(side=TOP, padx=5, fill=BOTH, expand=True)

msg_content_textbox = Text(msg_content_container, bg="white", font=smaller_body_text, width=50, height=10, wrap=WORD)
update_decoded_msg_textbox(msg_content_textbox, "")
msg_content_textbox.pack(fill=BOTH, expand=True)


# ----------------------
decode_root.protocol("WM_DELETE_WINDOW", decode_root.quit)
decode_root.mainloop()