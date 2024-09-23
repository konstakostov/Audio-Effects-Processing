import tkinter as tk

from GUI.Window.Top_Window_Visualisation.Top_Window_Phase_Spectrum.top_window_phase_spectrum_plot import \
    top_window_phase_spectrum_creation

"""
The 'create_phase_visualisation_button' function is used to define and position the button for the phase spectrum graph.

The 'phase_visualisation_button_functionality' function is used to add functionality to the created button.
The 'top_window_phase_spectrum_creation' function is called to create the phase spectrum visualisation.
"""


def create_phase_visualisation_button(self):
    choose_wav_to_visualise_button = tk.Button(
        self,
        text="Phase Spectrum Graph",
        command=phase_visualisation_button_functionality
    )

    choose_wav_to_visualise_button.grid(
        row=8,
        column=5,
        padx=10,
        pady=10,
        sticky="W",
    )


def phase_visualisation_button_functionality():
    top_window_phase_spectrum_creation()
