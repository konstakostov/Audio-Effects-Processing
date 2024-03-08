import tkinter as tk
from tkinter import messagebox, filedialog

import matplotlib.pyplot as plt
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np

from scipy.io import wavfile
from scipy.signal import spectrogram

from GUI.Variables.stored_variables import VariableStorage

"""
The 'top_window_spectrogram_creation' function creates the top window which shows the spectrogram visualisation.
If there is no audio file selected the user an error is raised and the user is prompted to select a .wav file to 
visualise.
If there is selected .wav file a Top Window is created. The .wav file is read and the sampling frequency ('fs' variable) 
and the audio data ('audio_data' variable) are determined. After that we are limiting the audio data to only 1 channel.
After that the Spectrogram is plotted, using the 'spectrogram' function and, as arguments are provided:
- 'audio_data': The input audio signal.
- 'fs': Sampling frequency.
- 'nperseg': Number of samples in each segment.
- 'noverlap': Number of samples that each segment overlaps with the previous one.
- 'window': Windowing function applied to each segment before computing the Fourier transform.

The 'sxx' variable is the computed spectrogram matrix, and a small constant is added to avoid division by zero. The plot 
is created using the 'pcolormesh' function, which takes time, frequencies, logarithmic intensity and spectrogram shading 
as parameters. The function 'colorbar' adds a colorbar to the plot, which can be used as a legend to determine the 
intensity, in dB, of the spectrogram. The 'canvas' variable is used to create a canvas, that is used to embedd the plot 
to the Top Window, which is then packed, based on the Top Window dimensions. The 'toolbar' variable is create a native 
matplotlib toolbar and add it to Top Window, which provides additional functionalities to the created plot. 

The 'save_callback' function is a custom callback function. It overrides the "Save" button from the toolbar and allows 
the user to save the plot as .png or .jpg file in directory defined by the user. 'toolbar.save_figure' is used to 
override the "Save" button. 

'canvas.get_tk_widget().pack()' is used to pack the Matplotlib canvas in the Top Window for display.
"""


def top_window_spectrogram_creation():
    file_to_visualise_path = VariableStorage.file_path_visualise_wav_file

    if not file_to_visualise_path:
        messagebox.showerror(
            "Error",
            "No .wav file selected. \n"
            "\nPlease select a .wav to visualise!")
    else:
        top_window = tk.Toplevel()
        top_window.title("Spectrogram Visualization")

        sample_rate, audio_data = wavfile.read(file_to_visualise_path)
        audio_data = audio_data[:, 0]

        frequencies, times, sxx = spectrogram(
            audio_data,
            fs=sample_rate,
            nperseg=3000,
            noverlap=1024,
            window='hann'
        )

        sxx = np.maximum(sxx, 1e-10)

        fig = plt.figure()
        plt.pcolormesh(times, frequencies, 10 * np.log10(sxx), shading='gouraud')
        plt.colorbar(label='Intensity [dB]')
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [s]')
        plt.title('Spectrogram')
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=top_window)
        canvas.draw()
        canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(canvas, top_window)
        toolbar.update()
        canvas.get_tk_widget().pack()

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
