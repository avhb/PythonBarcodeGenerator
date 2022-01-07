import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning. -> not for this application -> empty build options
build_exe_options = {"excludes": ["tkinter"]}

# base = None for terminal applications
base = None

setup(  name = "python-barcode-generator",
        version = "0.1.0",
        description = "Generates code128 barcodes, use --help for options",
        options = {"build_exe": build_exe_options},
        executables = [Executable("python-barcode-generator.py", base=base)])