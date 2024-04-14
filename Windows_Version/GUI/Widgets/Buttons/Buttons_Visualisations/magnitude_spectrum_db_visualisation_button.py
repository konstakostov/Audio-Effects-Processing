import tkinter as tk

from Windows_Version.UI.Window.Top_Window_Visualisation.Top_Window_Magnitude_Spectrum_dB.top_window_magnitude_db_spectrum_plot import \
    top_window_magnitude_db_spectrum_creation

"""
The 'create_magnitude_db_visualisation_button' function is used to define and position the button for the magnitude 
spectrum graph in dB.

The 'magnitude_db_visualisation_button_functionality' function is used to add functionality to the created button.
The 'top_window_magnitude_db_spectrum_creation' function is called to create the magnitude spectrum in dB visualisation.
"""


def create_magnitude_db_visualisation_button(self):
    choose_wav_to_visualise_button = tk.Button(
        self,
        text="Magnitude [dB] Spectrum Graph",
        command=magnitude_db_visualisation_button_functionality
    )

    choose_wav_to_visualise_button.grid(
        row=5,
        column=5,
        padx=10,
        pady=10,
        sticky="W",
    )


def magnitude_db_visualisation_button_functionality():
    top_window_magnitude_db_spectrum_creation()
