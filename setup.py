import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.

build_exe_options = {"packages": ['pyttsx3','AppOpener','geopy','googletrans','smtplib','pyautogui','pycaw','comtypes']}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "MyJarvis",
    version = "0.1",
    description = "My Jarvis AI application!",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base=base)]
)