import tkinter as tk

from GUI.Widgets.Buttons_Functionality.choose_wav_file_button_functionality import choose_wav_file_button_functionality


def define_choose_wav_file_button(self):
    # Variable to hold the button for choosing .wav to process
    choose_wav_button = tk.Button(
        self,
        text="Select .wav File",
        command=choose_wav_file_button_functionality
    )

    # Positioning the button for choosing .wav file
    choose_wav_button.grid(
        row=9,
        column=0,
        columnspan=2,
        padx=10,
        pady=10,
    )
