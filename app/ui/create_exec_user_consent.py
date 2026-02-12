# coding: utf-8

from pathlib import Path
import sys
from tkinter import *

path_root = Path(__file__).parents[2]
sys.path.insert(0, str(path_root))
from app.ui.fonts_properties import *

def run_create_exec_user_consent_ui(parent_window):
    # ----------------------
    # MAIN WINDOW SETUP
    # ----------------------
    user_consent_root = Toplevel(parent_window)
    user_consent_root.title("User consent")
    user_consent_root.geometry("+100+100")
    user_consent_root.wm_attributes("-toolwindow", True)

    # ----------------------
    # MINIMAL EVENT FUNCTIONS
    # ----------------------

    # ----------------------
    # ICONS / CANVAS LOADING
    # ----------------------

    # ----------------------
    # TITLE SECTION
    # ----------------------
    header_frame = Frame(user_consent_root, bg="white", bd=0, relief="flat")
    header_frame.pack(side=TOP, fill=X)

    header_title_container = Frame(header_frame, bg="white")
    header_title_container.pack(padx=20, pady=5, fill=X)

    title_header_label = Label(header_title_container, text="Guidelines about executables", bg="white", font=header_title)
    title_header_label.pack(side=LEFT)

    title_desc_label = Label(header_frame, text="Please read carefully the information below before proceeding.", bg="white", font=desc_text, wraplength=750, justify=CENTER)
    title_desc_label.pack(side=LEFT, padx=20, pady=5)


    # ----------------------
    # BODY SECTION
    # ----------------------

    body_frame = Frame(user_consent_root, bg="#f0f0f0", bd=2, borderwidth=2, relief="flat")
    body_frame.pack(fill=BOTH, pady=5, expand=True)

    part1_header = Label(body_frame, text="1. Safety Disclaimer", bg="#f0f0f0", font=header_subtitle)
    part1_header.pack(padx=20, pady=5, anchor=W)

    safety_textbox = Text(body_frame, bg="#ffffff", font=smaller_body_text, wrap=WORD, width=120, height=10, bd=2, relief="flat")
    safety_textbox.insert(END, "You are about to create an executable file from the decoded message. Stegano cannot ensure the legitimacy of the decoded script, nor can guarantee that the resulting executable will be free of malicious code.\nI, the developer of Stegano, disclaim any responsibility for any harm or damage that may arise from the use of the generated executable.\nPlease do not proceed if you are unsure about the safety of the decoded content or if you do not trust the source of the message.\n\nProceeding with the creation of the executable implies that you have read and understood this disclaimer, and that you accept full responsibility for any consequences that may result from running the generated executable.\n\nBy clicking the 'Create executable' button, Stegano will generate an executable file based on the decoded message and save it into your Downloads' folder. Stegano uses the 'cx_Freeze' Python library to create the executable.")
    safety_textbox.config(state=DISABLED)
    safety_textbox.pack(padx=20, pady=10, fill=BOTH, expand=True)


    part2_header = Label(body_frame, text="2. Terms of Use", bg="#f0f0f0", font=header_subtitle)
    part2_header.pack(padx=20, pady=5, anchor=W)

    terms_textbox = Text(body_frame, bg="#ffffff", font=smaller_body_text, wrap=WORD, width=120, height=10, bd=2, relief="flat")
    terms_textbox.insert(END, "The generated executable is intended for educational and ethical use only. Do not use Stegano in any way that violates applicable laws or regulations, or for any malicious or harmful purposes.\n\nBy using Stegano to create an executable, you agree to use it responsibly and ethically, and to respect the rights and privacy of others. Do not use the generated executable to distribute malware, engage in unauthorized access, or cause harm to individuals or organizations.\n\nStegano is a tool designed for learning and experimentation in the field of steganography.")
    terms_textbox.config(state=DISABLED)
    terms_textbox.pack(padx=20, pady=10, fill=BOTH, expand=True)

    # ----------------------
    # USER CONSENT SECTION
    # ----------------------
    user_consent = BooleanVar()
    consent_checkbox = Checkbutton(body_frame, text="I have read and understood the above information, and I accept the terms and conditions for creating an executable.", variable=user_consent, bg="#f0f0f0", font=desc_text_bold, wraplength=750, justify=LEFT, command=lambda: create_executable_button.config(state=NORMAL if user_consent.get() else DISABLED))
    consent_checkbox.pack(padx=20, pady=10, anchor=W)

    create_executable_button = Button(body_frame, text="Create executable", font=button_text, state=DISABLED, command=lambda: user_consent_root.destroy())
    create_executable_button.pack(padx=20, pady=10, anchor=E)

    user_consent_root.protocol("WM_DELETE_WINDOW", user_consent_root.destroy)
    user_consent_root.transient(parent_window)
    user_consent_root.grab_set()
    parent_window.wait_window(user_consent_root)

    return user_consent.get()

# testing
if __name__ == "__main__":
    root = Tk()
    root.withdraw()  # Hide the main window
    run_create_exec_user_consent_ui(root)