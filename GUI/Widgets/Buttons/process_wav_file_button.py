import tkinter as tk

from GUI.Widgets.Buttons_Functionality.process_wav_file_button_functionality import \
    process_wav_file_button_functionality


def define_process_wav_file_button(self):
    # Variable to hold the button for processing the .wav file
    process_wav_button = tk.Button(
        self,
        text="Process Audio File",
        command=process_wav_file_button_functionality
    )

    # Positioning the button for processing the .wav file
    process_wav_button.grid(
        row=9,
        column=2,
        columnspan=2,
        padx=10,
        pady=10,
    )