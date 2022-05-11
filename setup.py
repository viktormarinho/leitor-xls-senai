from pydoc import describe
from cx_Freeze import setup, Executable
import sys

build = {"packages": ["os","pysimplegui","pandas","openpyxl","xlrd"], "excludes": []}

base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(
    name="Leitor Planilhas",
    version="0.1",
    description= "",
    options = {"build.exe": build},
    executables = [Executable("ChooseFile.py", base = base)]
)