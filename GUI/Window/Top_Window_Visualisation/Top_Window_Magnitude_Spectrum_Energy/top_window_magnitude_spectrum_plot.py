import tkinter as tk
from tkinter import messagebox, filedialog

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from scipy.io import wavfile

from GUI.Variables.stored_variables import VariableStorage

"""
The 'top_window_magnitude_spectrum_creation' function creates the top window which shows the magnitude spectrum 
visualisation.
If there is no audio file selected the user an error is raised and the user is prompted to select a .wav file to 
visualise.
If there is selected .wav file a Top Window is created. The .wav file is read and the sampling frequency ('fs' variable) 
and the audio data ('audio_data' variable) are determined. After that we are limiting the audio data to only 1 channel.
After that the Magnitude Spectrum is plotted, using the 'magnitude_spectrum' function and, as arguments, the audio 
data and sampling frequency, while setting the scale to 'dB'. To the plot are added title and labels (to x and y 
dimensions). The 'canvas' variable is used to create a canvas, that is used to embedd the plot to the Top Window, which 
is then packed, based on the Top Window dimensions. The 'toolbar' variable is create a native matplotlib toolbar and add 
it to Top Window, which provides additional functionalities to the created plot. 

The 'save_callback' function is a custom callback function. It overrides the "Save" button from the toolbar and allows 
the user to save the plot as .png or .jpg file in directory defined by the user. 'toolbar.save_figure' is used to 
override the "Save" button. 

'canvas.get_tk_widget().pack()' is used to pack the Matplotlib canvas in the Top Window for display.
"""


def top_window_magnitude_spectrum_creation():
    file_to_visualise_path = VariableStorage.file_path_visualise_wav_file

    if not file_to_visualise_path:
        messagebox.showerror(
            "Error",
            "No .wav file selected. \n"
            "\nPlease select a .wav to visualise!")
    else:
        top_window = tk.Toplevel()
        top_window.title("Magnitude [dB] Spectrum Visualization")

        fs, audio_data = wavfile.read(file_to_visualise_path)
        audio_data = audio_data[:, 0]

        fig, ax = plt.subplots()
        ax.magnitude_spectrum(audio_data, Fs=fs, scale='dB')
        ax.set_title("Magnitude [dB] Spectrum Graph")
        ax.set_xlabel("Magnitude [energy]")
        ax.set_ylabel("Frequency")

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


