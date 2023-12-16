import os
import tkinter as tk
from tkinter import filedialog

from GUI.effects_data import EffectGroups
from GUI.functions import MainCheckboxFunctions, MainButtonFunctions
from GUI.top_windows import SecondaryWindow
from GUI.widgets import MainCheckbox


# Main Window
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Sets window title
        self.title("Audio Effects Processing")

        # Sets initial size (width, height) to 50% of screen size
        window_width = self.winfo_screenwidth() * 0.50
        window_height = self.winfo_screenheight() * 0.50

        # Center window on Users screen
        position_top = int(self.winfo_screenheight() / 2 - window_height / 2)
        position_right = int(self.winfo_screenwidth() / 2 - window_width / 2)

        self.geometry("%dx%d+%d+%d" % (window_width, window_height, position_right, position_top))

        # Makes window resizable
        self.resizable(True, True)

        # Variable to hold the button for choosing .wav to process
        select_file_button = tk.Button(
            self,
            text="Select .wav File",
            command=self.select_wav_file_to_process
        )

        # Positioning the button for choosing .wav file
        select_file_button.grid(
            row=9,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
        )

        # Variable to hold the button for processing the .wav file
        process_button = tk.Button(
            self,
            text="Process Audio File",
            command=self.get_saved_effects
        )

        # Positioning the button for processing the .wav file
        process_button.grid(
            row=9,
            column=2,
            columnspan=2,
            padx=10,
            pady=10,
        )

        # It takes start_row, end_row, column, frame_label, effects name labels as parameters
        self.create_frames([
            # First Frame 'Guitar Effects'
            (1, 5, 0, 'Guitar-Style Effects', EffectGroups.guitar_effects),
            # Second Frame Dynamic Range Effects'
            (6, 9, 0, 'Dynamic Range Effects', EffectGroups.dynamic_range_effects),
            # Third Frame 'Equalizers and Filters'
            (1, 4, 2, 'Equalizers and Filters', EffectGroups.eq_filter_effects),
            # Fourth Frame 'Spatial Effects'
            (5, 7, 2, 'Spatial Effects', EffectGroups.spatial_effects),
            # Fifth Frame 'Pitch Effects'
            (8, 9, 2, 'Pitch Effects', EffectGroups.pitch_effects)
        ])

    # Function to select .wav file to process
    @staticmethod
    def select_wav_file_to_process():
        # Getting the current directory
        current_dir = os.getcwd()

        # Opening a file dialog to select a .wav file
        file_path = filedialog.askopenfilename(
            # Initial directory
            initialdir=current_dir,
            # Title of file dialog window
            title="Select .wav File",
            # Filtering to display only .wav files
            filetypes=(("WAV files", "*.wav"), ("All files", "*.*")),
        )

        # # Display file path chosen
        # if file_path:
        #     print("Selected .wav file:", file_path)

    # Getting all saved effects and their parameters
    @staticmethod
    def get_saved_effects():
        saved_parameters = SecondaryWindow.saved_effect_parameters

    # Creating all frames
    def create_frames(self, frames):
        for frame in frames:
            self.main_frames(*frame)

    # Creating a single frame
    def main_frames(self, start_row, end_row, column, frame_label, checkbox_labels):
        # A frame is created to store the layer and min size is set for it
        main_frame = tk.Frame()
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid(sticky='EW')

        # A label to visualise the frame's effects, and it's positioned in the window.
        tk.Label(
            self,
            text=frame_label,
            font=('Segoe UI', '10', 'bold',),
        ).grid(
            row=start_row - 1,
            column=column,
            padx=10,
            pady=10,
            sticky='W',
        )

        # In the rows in range 'start_row' - 'end_row' are created checkboxes and buttons.
        # When the checkbox is activated, it enables the button.
        # The checkbox is positioned in column 'column', and the button in column 'column' + 1.
        for i in range(start_row, end_row):
            main_frame.grid_rowconfigure(i, weight=1, pad=10)

            # Variable to hold the checkbox
            checkbox = MainCheckbox(
                self,
                text=checkbox_labels[i - start_row],
                callback=MainCheckboxFunctions.on_checkbox_change,
            )

            # Positioning the checkbox
            checkbox.grid(
                row=i,
                column=column,
            )

            # Positioning the button for the checkbox
            checkbox.button.grid(
                row=i,
                column=column + 1,
                padx=10,
                pady=10,
            )

            # Adding functionality to the checkbox button
            checkbox.button.config(
                command=lambda text=checkbox_labels[i - start_row]:
                MainButtonFunctions.set_parameters_button(text)
            )


# Makes the window stay on screen until the user closes it.
# Without this the program will start and close, without the user noticing.
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
