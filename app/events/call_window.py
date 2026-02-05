import subprocess

def call_app_window():
    """Call the main application window."""
    subprocess.run(["python3", "app/ui/app_ui.py"])

def call_encode_window():
    """Call the encoding window."""
    subprocess.run(["python3", "app/ui/encode.py"])

def call_decode_window():
    """Call the decoding window."""
    subprocess.run(["python3", "app/ui/decode.py"])