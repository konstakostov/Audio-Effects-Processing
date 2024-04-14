import tkinter as tk
from tkinter import messagebox

from Windows_Version.Effects.Effects_Essential_Processes.convert_saved_parameters_for_pedalboard import convert_effect_parameters
from Windows_Version.Effects.virtual_pedalboard import create_virtual_pedalboard
from Windows_Version.GUI.Variables.stored_variables import VariableStorage

"""
The 'define_process_wav_file_button' function is used to define and position the button which will start the processing 
of the selected .wav file.

The 'process_wav_file_button_functionality' function is used to add functionality to the created button.
The 'transformed_parameters' variable is used to store and transform the parameters of the selected effects.
The 'audio_path' variable is used to call and store the path of the selected input .wav file.
The 'saved_parameters' variable is used to call and store the saved parameters of the selected effects.
The 'error_is_raised' variable is used to check if the and error message has been raised.
If 'audio_path' variable is None an error is raised prompting the user to select .wav file to be processed.
If 'saved_parameters' variable is None an error is raised prompting the user to select effects to process the .wav file 
with. If no error is raised the selected effects are transformed into appropriate Pedalboard objects and the 
'saved_effect_parameters' variable is cleared not to interfere with the next .wav file to be processed.
If no errors are raised the 'create_virtual_pedalboard' function is called to create process the .wav file with the 
selected effects.
"""


def define_process_wav_file_button(self):
    process_wav_button = tk.Button(
        self,
        text="Process Audio File",
        command=process_wav_file_button_functionality
    )

    process_wav_button.grid(
        row=9,
        column=2,
        columnspan=2,
        padx=10,
        pady=10,
    )


def process_wav_file_button_functionality():
    transformed_parameters = None

    audio_path = VariableStorage.file_path_selected_wav_file
    saved_parameters = VariableStorage.saved_effect_parameters

    error_is_raised = False

    if audio_path is None:
        messagebox.showerror(
            "Error",
            "No input file selected!")
        error_is_raised = True

    if not saved_parameters:
        messagebox.showerror(
            "Error",
            "No audio effects selected!")
        error_is_raised = True
    else:
        transformed_parameters = convert_effect_parameters(saved_parameters)

        VariableStorage.saved_effect_parameters = {}

    if not error_is_raised:
        create_virtual_pedalboard(transformed_parameters, audio_path)
