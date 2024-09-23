import tkinter as tk

from GUI.Window.Top_Window_Visualisation.Top_Window_Magnitude_Spectrum_Energy.top_window_magnitude_spectrum_plot import \
    top_window_magnitude_spectrum_creation

"""
The 'create_magnitude_energy_visualisation_button' function is used to define and position the button for the magnitude 
spectrum graph.

The 'magnitude_energy_visualisation_button_functionality' function is used to add functionality to the created button.
The 'top_window_magnitude_spectrum_creation' function is called to create the magnitude spectrum visualisation.
"""


def create_magnitude_energy_visualisation_button(self):
    choose_wav_to_visualise_button = tk.Button(
        self,
        text="Magnitude Spectrum Graph",
        command=magnitude_energy_visualisation_button_functionality
    )

    choose_wav_to_visualise_button.grid(
        row=6,
        column=5,
        padx=10,
        pady=10,
        sticky="W",
    )


def magnitude_energy_visualisation_button_functionality():
    top_window_magnitude_spectrum_creation()
