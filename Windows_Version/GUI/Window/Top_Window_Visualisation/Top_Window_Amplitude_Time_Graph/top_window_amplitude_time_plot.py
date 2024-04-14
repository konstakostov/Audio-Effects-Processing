import tkinter as tk
from tkinter import messagebox, filedialog

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

import numpy as np
from scipy.io import wavfile

from Windows_Version.GUI.Variables.stored_variables import VariableStorage

"""
The 'top_window_amplitude_time_creation' function creates the top window which shows the amplitude-time graph 
visualisation.
If there is no audio file selected the user an error is raised and the user is prompted to select a .wav file to 
visualise.
If there is selected .wav file a Top Window is created. The .wav file is read and the sampling frequency ('fs' variable) 
and the audio data ('audio_data' variable) are determined. The 'time_array' variable holds the time values, 
corresponding to each sample in the audio data. After that the Amplitude-Time Graph is plotted, using the time array and
the audio data as arguments. To the plot are added title and labels (to x and y dimensions). The 'canvas' variable is 
used to create a canvas, that is used to embedd the plot to the Top Window, which is then packed, based on the Top 
Window dimensions. The 'toolbar' variable is create a native matplotlib toolbar and add it to Top Window, which provides 
additional functionalities to the created plot. 

The 'save_callback' function is a custom callback function. It overrides the "Save" button from the toolbar and allows 
the user to save the plot as .png or .jpg file in directory defined by the user. 'toolbar.save_figure' is used to 
override the "Save" button. 

'canvas.get_tk_widget().pack()' is used to pack the Matplotlib canvas in the Top Window for display.
"""


def top_window_amplitude_time_creation():
    file_to_visualise_path = VariableStorage.file_path_visualise_wav_file

    if not file_to_visualise_path:
        messagebox.showerror(
            "Error",
            "No .wav file selected. \n"
            "\nPlease select a .wav to visualise!")
    else:
        top_window = tk.Toplevel()
        top_window.title("Amplitude-Time Graph Visualization")

        fs, audio_data = wavfile.read(file_to_visualise_path)

        time_array = np.arange(0, len(audio_data)) / fs

        fig, ax = plt.subplots()
        ax.plot(time_array, audio_data)
        ax.set_title("Amplitude-Time Graph")
        ax.set_xlabel("Time [s]")
        ax.set_ylabel("Amplitude [Samples]")

        canvas = FigureCanvasTkAgg(fig, master=top_window)
        canvas.draw()
        canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(canvas, top_window)
        toolbar.update()
        toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        def save_callback():
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[
                    ("PNG files", "*.png"),
                    ("JPEG files", "*.jpg"),
                    ("All files", "*.*")
                ]
            )
            if file_path:
                fig.savefig(file_path, bbox_inches='tight', pad_inches=0.1)

        toolbar.save_figure = save_callback

        canvas.get_tk_widget().pack()


