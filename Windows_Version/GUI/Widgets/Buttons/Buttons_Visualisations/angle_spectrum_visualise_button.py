import tkinter as tk

from GUI.Window.Top_Window_Visualisation.Top_Window_Angle_Spectrum.top_window_angle_spectrum_plot import \
    top_window_angle_spectrum_creation

"""
The 'create_angle_visualisation_button' function is used to define and position the button for the angle visualisation
graph.

The 'angle_visualisation_button_functionality' function is used to add functionality to the created button.
The 'top_window_angle_spectrum_creation' function is called to create the angle spectrum visualisation.
"""


def create_angle_visualisation_button(self):
    choose_wav_to_visualise_button = tk.Button(
        self,
        text="Angle Spectrum Graph",
        command=angle_visualisation_button_functionality
    )

    choose_wav_to_visualise_button.grid(
        row=7,
        column=5,
        padx=10,
        pady=10,
        sticky="W",
    )


def angle_visualisation_button_functionality():
    top_window_angle_spectrum_creation()
