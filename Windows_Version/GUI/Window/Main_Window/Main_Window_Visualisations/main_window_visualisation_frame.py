import tkinter as tk

from Windows_Version.GUI.Widgets.Buttons.Buttons_Visualisations.amplitude_time_visualisation_button import \
    create_amplitude_time_visualisation_button
from GWindows_Version.UI.Widgets.Buttons.Buttons_Visualisations.angle_spectrum_visualise_button import \
    create_angle_visualisation_button
from Windows_Version.GUI.Widgets.Buttons.Buttons_Visualisations.choose_wav_file_to_visualise_button import \
    define_choose_wav_file_to_visualise_button
from Windows_Version.GUI.Widgets.Buttons.Buttons_Visualisations.magnitude_spectrum_db_visualisation_button import \
    create_magnitude_db_visualisation_button
from Windows_Version.GUI.Widgets.Buttons.Buttons_Visualisations.magnitude_spectrum_energy_visualisation_button import \
    create_magnitude_energy_visualisation_button
from Windows_Version.GUI.Widgets.Buttons.Buttons_Visualisations.phase_spectrum_visualisation_button import \
    create_phase_visualisation_button
from Windows_Version.GUI.Widgets.Buttons.Buttons_Visualisations.spectrogram_visualisation_button import \
    create_spectrogram_visualisation_button

"""
The 'create_main_window_visualisation_frame' function is used to create a frame for the Main Window. The weight for 
each of columns in the frame is set to 1.

The 'define_choose_wav_file_to_visualise_button' function is used to create a button, which when pressed prompts the 
user to choose a .wav file to be visualised. 

The 'create_amplitude_time_visualisation_button' function is used to create a button, which when pressed opens a top 
window with the amplitude-time graph of the chosen .wav file.

The 'create_spectrogram_visualisation_button' function is used to create a button, which when pressed opens a top 
window with the spectrogram of the chosen .wav file.

The 'create_magnitude_db_visualisation_button' function is used to create a button, which when pressed opens a top 
window with the magnitude spectrum [dB] of the chosen .wav file.

The 'create_magnitude_energy_visualisation_button' function is used to create a button, which when pressed opens a top 
window with the magnitude spectrum [Energy] spectrum of the chosen .wav file.

The 'create_phase_visualisation_button' function is used to create a button, which when pressed opens a top 
window with the phase spectrum of the chosen .wav file.

The 'create_angle_visualisation_button' function is used to create a button, which when pressed opens a top 
window with the angle spectrum of the chosen .wav file.
"""


def create_main_window_visualisation_frame(parent):
    main_window_frame = tk.Frame(parent)
    main_window_frame.grid_columnconfigure(0, weight=1)
    main_window_frame.grid(sticky="EW")

    define_choose_wav_file_to_visualise_button(parent)

    create_amplitude_time_visualisation_button(parent)

    create_spectrogram_visualisation_button(parent)

    create_magnitude_db_visualisation_button(parent)

    create_magnitude_energy_visualisation_button(parent)

    create_phase_visualisation_button(parent)

    create_angle_visualisation_button(parent)
