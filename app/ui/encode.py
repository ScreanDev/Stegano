# coding: utf-8

from pathlib import Path
import sys
from tkinter import *
from fonts_properties import *

path_root = Path(__file__).parents[2]
sys.path.insert(0, str(path_root))
from app.events.common_events import load_encoding_ui, select_file_in_explorer, resource_path
from app.main import encode_process

file_path = ""


# ----------------------
# MAIN WINDOW SETUP
# ----------------------
encode_root = Tk()
encode_root.title("Encode a message within an image")
encode_root.geometry("800x500")


# ----------------------
# MINIMAL EVENT FUNCTIONS
# ----------------------

def img_selection_event():
    """
    Handle the event when the user clicks the "Browse..." button to select an image file for encoding.
    Once selected, load the preview UI.
    """
    global file_path
    previous_file_path = file_path # Store the previous file path to check if the user cancelled the file selection dialog
    file_path = select_file_in_explorer(file_formats=("Images", "*.png *.jpg *.jpeg"))

    if not (file_path == None or file_path == ""):
        # UI loading
        load_encoding_ui(img_select_frame, resource_path(file_path), encode_ready_frame)
    else:
        file_path = previous_file_path # If the user cancelled the dialog, keep the previous file path


# ----------------------
# ICONS / CANVAS LOADING
# ----------------------
encode_icon = PhotoImage(file=resource_path("app/assets/ui/encode_icon.png"))
decode_icon = PhotoImage(file=resource_path("app/assets/ui/decode_icon.png"))


# ----------------------
# TITLE SECTION
# ----------------------
header_frame = Frame(encode_root, bg="white", bd=0, relief="flat")
header_frame.pack(side=TOP, fill=X, pady=10)

header_title_container = Frame(header_frame, bg="white")
header_title_container.pack(expand=True)

encode_icon_canvas = Canvas(header_title_container, width=100, height=25, bd=0, bg="white", highlightthickness=0)
encode_icon_canvas.create_image(0, 0, anchor=NW, image=encode_icon)
encode_icon_canvas.pack(side=LEFT, pady=5)

title_header_label = Label(header_title_container, text="Encoding", bg="white", font=header_subtitle)
title_header_label.pack(side=LEFT, padx=10)

title_desc_label = Label(header_frame, text="Encode a message into an image file seamlessly. You can even inject Python scripts within the picture, then execute it by decoding the generated image.", bg="white", font=desc_text, wraplength=750, justify=CENTER)
title_desc_label.pack(side=BOTTOM, pady=5)


# ----------------------
# BODY SECTION
# ----------------------
body_frame = Frame(encode_root, bg="#f0f0f0", bd=2, borderwidth=2, relief="flat")
body_frame.pack(fill=BOTH, pady=5, expand=True)

# ----------------------
# MESSAGE INPUT
# ----------------------
message_input_frame = Frame(body_frame, bg="#f0f0f0", bd=2, borderwidth=1, relief="solid")
message_input_frame.pack(side=LEFT, padx=10, fill=BOTH, expand=True)

msg_title_container = Frame(message_input_frame, bg="#f0f0f0")
msg_title_container.pack(side=TOP, padx=20, pady=5, fill=X)

msg_title_label = Label(msg_title_container, text="Enter the message to encode:", bg="#f0f0f0", font=smaller_body_text, wraplength=300, justify=LEFT)
msg_title_label.pack(side=LEFT)

msg_content_container = Frame(message_input_frame, bg="#f0f0f0")
msg_content_container.pack(side=TOP, padx=20, pady=5, fill=BOTH, expand=True)

msg_textbox = Text(msg_content_container, bg="white", font=smaller_body_text, width=50, height=10, wrap=WORD)
msg_textbox.pack(fill=BOTH, expand=True)

mark_as_script_tick = BooleanVar()
mark_as_script_checkbox = Checkbutton(msg_content_container, text="Mark as a Python script", variable=mark_as_script_tick, bg="#f0f0f0", font=smaller_body_text)
mark_as_script_checkbox.pack(side=TOP, pady=5, anchor=W)


# ----------------------
# IMAGE SELECTION
# ----------------------
img_select_frame = Frame(body_frame, bg="#f0f0f0", bd=2, borderwidth=1, relief="solid")
img_select_frame.pack(side=RIGHT, padx=10, fill=BOTH, expand=True)

img_title_container = Frame(img_select_frame, bg="#f0f0f0")
img_title_container.pack(side=TOP, padx=20, pady=5, fill=X)

img_title_label = Label(img_title_container, text="Select an image file to use for encoding:", bg="#f0f0f0", font=smaller_body_text, wraplength=200, justify=LEFT)
img_title_label.pack(side=LEFT)

img_btn_container = Frame(img_select_frame, bg="#f0f0f0")
img_btn_container.pack(side=TOP, padx=20, pady=5, fill=X)

img_select_btn = Button(img_btn_container, text="Browse...", bg="white", font=button_text, command=img_selection_event)
img_select_btn.pack(side=LEFT)


# ----------------------
# READY-TO-ENCODE SECTION
# ----------------------
encode_ready_frame = Frame(encode_root, bg="lightgray", bd=2, borderwidth=2, relief="flat")

encode_ready_label = Label(encode_ready_frame, text="Ready to encode your message!", bg="lightgray", font=bold_body_text)
encode_ready_label.pack(side=LEFT, padx=30, pady=10)

encode_button = Button(encode_ready_frame, text="Encode Message", font=button_text, command=lambda: encode_process(img_path=resource_path(file_path), message=msg_textbox.get("1.0", END), is_script=mark_as_script_tick.get()))
encode_button.pack(side=LEFT, padx=20, pady=10)


# ----------------------

encode_root.protocol("WM_DELETE_WINDOW", encode_root.quit)
encode_root.mainloop()