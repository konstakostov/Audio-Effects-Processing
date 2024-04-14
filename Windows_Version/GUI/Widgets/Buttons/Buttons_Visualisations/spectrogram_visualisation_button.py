import tkinter as tk

from GUI.Window.Top_Window_Visualisation.Top_Window_Spectrogram.top_window_spectrogram_plot import \
    top_window_spectrogram_creation

"""
The 'create_spectrogram_visualisation_button' function is used to define and position the button for 

The 'spectrogram_visualisation_button_functionality' function is used to add functionality to the created button.
The 'top_window_spectrogram_creation' function is called to create the spectrogram visualisation.
"""


def create_spectrogram_visualisation_button(self):
    choose_wav_to_visualise_button = tk.Button(
        self,
        text="Spectrogram",
        command=spectrogram_visualisation_button_functionality
    )

    choose_wav_to_visualise_button.grid(
        row=4,
        column=5,
        padx=10,
        pady=10,
        sticky="W",
    )


def spectrogram_visualisation_button_functionality():
    top_window_spectrogram_creation()
