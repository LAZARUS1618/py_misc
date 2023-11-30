# Ethan Gueck
# CONVERT PY TO EXE V1.2
# Created 11.7.2022
# This Script is intended to convert a pyw file which is a python file that does not open the command terminal to an
# executable. Script must be run as an administrator.

import os
import shutil
import subprocess

script_name = r'Convert_PY_TO_EXE.py'
script_name = script_name.replace("\\", "\\\\")
exe_name = 'FAT_APP'
icon_name = r'' # Insert file path
icon_name = icon_name.replace("\\", "\\\\")
temp_dir = os.path.join(os.path.expanduser('~'), 'Desktop', 'temp')
os.makedirs(temp_dir, exist_ok=True)
shutil.copy2(script_name, temp_dir)
shutil.copy2(icon_name, temp_dir)

# Use PyInstaller to convert the Python script to an executable file
subprocess.run(['pyinstaller', '--onefile', '--icon', icon_name, script_name], cwd=temp_dir) #, '--windowed'


# Move the executable file to the Desktop and rename it
exe_file = os.path.join(temp_dir, 'dist', script_name.replace('.pyw', '.exe'))
#exe_file = exe_file.replace("exew", "exe") Errors.
shutil.copy2(exe_file, os.path.join(os.path.expanduser('~'), 'Desktop', exe_name + '.exe')) #This may also Error.

# Clean up the temporary directory
shutil.rmtree(temp_dir)

