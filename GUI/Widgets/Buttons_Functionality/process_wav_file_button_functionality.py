# Getting all saved effects and their parameters
from tkinter import messagebox

from Effects.convert_saved_parameters_for_pedalboard import convert_effect_parameters
from Effects.virtual_pedalboard import create_virtual_pedalboard
from GUI.Variables.stored_variables import VariableStorage


def process_wav_file_button_functionality():
    # Declaring variables that are parameters for 'process_audio' function
    transformed_parameters = None
    # audio_name = None
    audio_path = None

    # Variable to get the used effects and their parameters
    saved_parameters = VariableStorage.saved_effect_parameters

    # If no input file path exists give error message to the user to select one
    if VariableStorage.file_path_selected_wav_file:
        # Assigning the file directory to the
        # variable for 'process_audio' parameters
        audio_path = VariableStorage.file_path_selected_wav_file
    else:
        messagebox.showerror(
            "Error",
            "No input file selected!")

    # If there are no effects and parameters
    # give error message to the user to select at least one
    if saved_parameters:
        # Assigning the effects and their parameters
        # to a variable for 'process_audio' parameters
        # after passing them to the 'transform_effect_parameters' function
        transformed_parameters = convert_effect_parameters(saved_parameters)

        # Clearing the 'saved_effect_parameters' dictionary
        # so the previously chosen effects do not affect
        # the next file to be processed
        VariableStorage.saved_effect_parameters = {}
    else:
        messagebox.showerror(
            "Error",
            "No audio effects selected!")

    # Processing the input file with the chosen effects
    create_virtual_pedalboard(transformed_parameters, audio_path)
