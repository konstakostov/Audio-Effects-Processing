# Function to select .wav file to process
import os
from tkinter import filedialog

from GUI.Variables.stored_variables import VariableStorage


def choose_wav_file_button_functionality():
    # Getting the current directory
    current_dir = os.getcwd()

    # Opening a file dialog to select a .wav file
    file_path = filedialog.askopenfilename(
        # Initial directory
        initialdir=current_dir,
        # Title of file dialog window
        title="Select .wav File",
        # Filtering to display only .wav files
        filetypes=(("WAV files", "*.wav"), ("All files", "*.*")),
    )

    # Checking if file path exist to determine the file to process
    if file_path:
        # Saving the input directory
        VariableStorage.file_path_selected_wav_file = file_path
