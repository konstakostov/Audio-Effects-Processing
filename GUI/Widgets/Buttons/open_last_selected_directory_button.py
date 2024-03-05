import tkinter as tk
from tkinter import messagebox

import subprocess
import os

from GUI.Variables.stored_variables import VariableStorage

"""
The 'define_open_last_directory_button' function is used to define and position the button which will open the directory 
of the last selected .wav file.

The 'open_last_directory_button_functionality' function is used to add functionality to the created button.
If there has been selected .wav file by the user then it will open it's directory, othwerwise it will raise and error 
to prompt the user to select a .wav file to process.
"""


def define_open_last_directory_button(self):
    choose_wav_button = tk.Button(
        self,
        text="Open Last Selected Directory",
        command=open_last_directory_button_functionality
    )

    choose_wav_button.grid(
        row=10,
        column=0,
        columnspan=2,
        padx=10,
        pady=10,
    )


def open_last_directory_button_functionality():
    if VariableStorage.file_path_selected_wav_file:
        last_selected_file = VariableStorage.file_path_selected_wav_file
        last_directory_path, last_selected_file_extension = os.path.split(last_selected_file)

        subprocess.Popen(['explorer', os.path.normpath(last_directory_path)])
    else:
        messagebox.showerror(
            "Error",
            "No last saved directory saved. \n"
            "\nPlease select input .wav file")
