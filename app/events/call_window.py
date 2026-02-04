import subprocess

def call_app_window():
    subprocess.run(["python3", "app/ui/app_ui.py"])

def call_encode_window():
    subprocess.run(["python3", "app/ui/encode.py"])