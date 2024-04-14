import tkinter as tk

from Windows_Version.GUI.Window.Top_Window_Visualisation.Top_Window_Amplitude_Time_Graph.top_window_amplitude_time_plot import \
    top_window_amplitude_time_creation

"""
The 'create_amplitude_time_visualization_button' function is used to define and position the button for amplitude-time 
graph.

The 'amplitude_time_visualization_button_functionality' function is used to add functionality to the created button.
The 'top_window_amplitude_time_creation' function is called to create the amplitude-time graph visualisation.
"""


def create_amplitude_time_visualisation_button(self):
    choose_wav_to_visualise_button = tk.Button(
        self,
        text="Amplitude-Time Graph",
        command=amplitude_time_visualisation_button_functionality
    )

    choose_wav_to_visualise_button.grid(
        row=3,
        column=5,
        padx=10,
        pady=10,
        sticky="W",
    )


def amplitude_time_visualisation_button_functionality():
    top_window_amplitude_time_creation()
