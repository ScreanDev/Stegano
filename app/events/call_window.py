import subprocess

def call_app_window():
    """Call the main application window."""
    # Local import
    from app.ui.app_ui import root
    # Running the main application window
    root.mainloop()

def call_encode_window(current_root):
    """Call the encoding window."""
    # Local import
    from app.ui.encode import run_encode_ui
    # Running the encode UI as a modal window
    run_encode_ui(current_root)

def call_decode_window(current_root):
    """Call the decoding window."""
    # Local import
    from app.ui.decode import run_decode_ui
    # Running the decode UI as a modal window
    run_decode_ui(current_root)