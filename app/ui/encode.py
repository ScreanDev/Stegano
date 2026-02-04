# coding: utf-8
 
from logging import root
from tkinter import *
from fonts_properties import *

# ----------------------
# MAIN WINDOW SETUP
# ----------------------
encode_root = Tk()
encode_root.title("Encode a message within an image")
encode_root.geometry("800x400")
encode_root.resizable(False, False)
encode_root.wm_attributes('-toolwindow', True)

# ----------------------
encode_root.mainloop()