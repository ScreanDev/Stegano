import sys
import os
from cx_Freeze import setup, Executable

# Defining the files to include in the build
files = [
    ("app/assets", "app/assets")  # Copy the entire assets folder
]

# Build options
build_exe_options = {
    "packages": ["os", "sys", "PIL", "tkinter"], # Force inclusion of Pillow and Tkinter
    "excludes": [],
    "include_files": files,
    "include_msvcr": True, # Include Visual C++ runtimes if needed
}

# Base management (GUI vs Console)
base = None
if sys.platform == "win32":
    base = "gui" # To hide the black console. Please remove this line to debug if needed

# Executable configuration
target = Executable(
    script="app/main.py", # Main file
    base=base,
    target_name="Stegano Tools.exe"
)

setup(
    name="Stegano Tools",
    version="1.0",
    description="Steganography Tool",
    options={"build_exe": build_exe_options},
    executables=[target]
)