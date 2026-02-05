# coding: utf-8
 
from pathlib import Path
import sys
from tkinter import *
from fonts_properties import *

path_root = Path(__file__).parents[2]
sys.path.insert(0, str(path_root))
from app.events.call_window import call_encode_window, call_decode_window

# ----------------------
# MAIN WINDOW SETUP
# ----------------------
root = Tk()
root.title("Stegano Tools")
root.geometry("800x400")
root.resizable(False, False)





# ----------------------
# ICONS / CANVAS LOADING
# ----------------------
encode_icon = PhotoImage(file="app/assets/ui/encode_icon.png")
decode_icon = PhotoImage(file="app/assets/ui/decode_icon.png")

# ----------------------
# MENUBAR SETUP
# ----------------------
menubar = Menu(root)
root.config(menu=menubar)

menu_about = Menu(menubar, tearoff=0)
menu_about.add_command(label="About")
menu_about.add_separator()
menu_about.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="Help", menu=menu_about)

# ----------------------
# TITLE SECTION
# ----------------------
header_frame = Frame(root, bg="white", bd=0, relief="flat")
header_frame.pack(side=TOP, fill=X, pady=10)

title_header_label = Label(header_frame, text="Stegano",bg="white", font=header_title)
title_header_label.pack()

title_desc_label = Label(header_frame, text="Use image files to hide and reveal secret messages.", bg="white", font=desc_text)
title_desc_label.pack()


# ----------------------
# ENCODE FRAME
# ----------------------
encode_frame = Frame(root, width=250, height=100, bg="#f0f0f0", bd=2, borderwidth=2, relief="flat")
encode_frame.pack(side=LEFT, pady=10, fill=BOTH, expand=True)

# Frame header
encode_header_frame = Frame(encode_frame, bg="white", bd=0, relief="flat")
encode_header_frame.pack(side=TOP, fill=X)

encode_header_center = Frame(encode_header_frame, bg="white", bd=0, relief="flat")
encode_header_center.pack(expand=True)

encode_icon_canvas = Canvas(encode_header_center, width=100, height=25, bd=0, bg="white", highlightthickness=0)
encode_icon_canvas.create_image(0, 0, anchor=NW, image=encode_icon)
encode_icon_canvas.pack(side=LEFT, pady=5)

encode_header_label = Label(encode_header_center, text="Encode", bg="white", font=body_text)
encode_header_label.pack(side=LEFT, padx=5)

# Frame body
encode_body_frame = Frame(encode_frame, bg="lightgrey", bd=0, relief="flat")
encode_body_frame.pack(side=BOTTOM, fill=BOTH, expand=True)

encode_body_desc = Label(encode_body_frame, text="Encode a message into an image file seamlessly. You can even inject Python scripts within the picture, then execute it by decoding the generated image.", bg="lightgrey", font=desc_text, wraplength=350, justify=LEFT)
encode_body_desc.pack(pady=5)

encode_button = Button(encode_body_frame, text="Encode an image", font=body_text, command=call_encode_window)
encode_button.pack(pady=10)

# ----------------------
# DECODE FRAME
# ----------------------
decode_frame = Frame(root, width=250, height=100, bg="#f0f0f0", bd=2, borderwidth=2, relief="flat")
decode_frame.pack(side=RIGHT, pady=10, fill=BOTH, expand=True)

# Frame header
decode_header_frame = Frame(decode_frame, bg="white", bd=0, relief="flat")
decode_header_frame.pack(side=TOP, fill=X)

decode_header_center = Frame(decode_header_frame, bg="white", bd=0, relief="flat")
decode_header_center.pack(expand=True)

decode_icon_canvas = Canvas(decode_header_center, width=100, height=25, bd=0, bg="white", highlightthickness=0)
decode_icon_canvas.create_image(0, 0, anchor=NW, image=decode_icon)
decode_icon_canvas.pack(side=LEFT, pady=5)

decode_header_label = Label(decode_header_center, text="Decode", bg="white", font=body_text)
decode_header_label.pack(side=LEFT, padx=5)

# Frame body
decode_body_frame = Frame(decode_frame, bg="lightgrey", bd=0, relief="flat")
decode_body_frame.pack(side=BOTTOM, fill=BOTH, expand=True)

decode_body_desc = Label(decode_body_frame, text="Import an image file to try decoding its hidden message. Scripts embedded within the image will be executed upon decoding.", bg="lightgrey", font=desc_text, wraplength=350, justify=LEFT)
decode_body_desc.pack(pady=5)

decode_button = Button(decode_body_frame, text="Decode an image", font=body_text, command=call_decode_window)
decode_button.pack(pady=10)


root.mainloop()