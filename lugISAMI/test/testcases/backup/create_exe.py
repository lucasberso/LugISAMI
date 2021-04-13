import sys
from cx_Freeze import setup, Executable

sys.argv.append("build")

# Dependencies are automatically detected, but it might need fine tuning.
additional_modules = []

build_exe_options = {"includes": additional_modules,
                     "packages": [],
                     "excludes": [],
                     "include_files": [],
                     'build_exe': '..\\exe\\'}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="lugISAMI",
      version="1.0",
      description="",
      options={"build_exe": build_exe_options},
      executables=[Executable(script="lugGUI.py", base=base)])