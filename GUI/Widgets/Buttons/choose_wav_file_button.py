import tkinter as tk
from tkinter import filedialog

import os

from GUI.Variables.stored_variables import VariableStorage

"""
The 'define_choose_wav_file_button' function is used to define and position the button for choosing the .wav file 
that is going to be processed.

The 'choose_wav_file_button_functionality' function is used to add functionality to the created button.
The variable 'current_dir' is used to get the current directory, where the project is placed.
The variable 'file_path' is used to open a file dialog, with starting directory as the current project directory.
The user can navigate from there to the desired directory and select any .wav file to be processed. 
If value in 'file_path' is valid the input file directory is saved in the specified variable.
"""


def define_choose_wav_file_button(self):
    choose_wav_button = tk.Button(
        self,
        text="Select .wav File",
        command=choose_wav_file_button_functionality
    )

    choose_wav_button.grid(
        row=9,
        column=0,
        columnspan=2,
        padx=10,
        pady=10,
    )


def choose_wav_file_button_functionality():
    current_dir = os.getcwd()

    file_path = filedialog.askopenfilename(
        initialdir=current_dir,
        title="Select .wav File",
        filetypes=(("WAV files", "*.wav"), ("All files", "*.*")),
    )

    if file_path:
        VariableStorage.file_path_selected_wav_file = file_path
