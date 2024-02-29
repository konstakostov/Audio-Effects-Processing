import tkinter as tk

from GUI.Widgets.Spinboxes.main_spinbox import MainSpinbox
from GUI.Window.Top_Window_Parameters.save_effect_parameters_function import save_effect_parameters


def top_window_parameters_frame_creation(top_window, effect_name, start_row, end_row, column, effect_parameters):
    # A frame is created to store the layer and min size is set for it
    top_window_parameters_frame = tk.Frame(top_window)
    top_window_parameters_frame.grid_columnconfigure(0, weight=1)
    top_window_parameters_frame.grid(sticky='EW')

    # List for storing all current spinbox objects
    spinbox_values = []

    # Iterating through each row and the effect parameter that it corresponds to
    for i in range(start_row, end_row):
        top_window_parameters_frame.grid_rowconfigure(i, weight=1, pad=10)

        # Creating the spinbox and defining bottom and top value
        spinbox = MainSpinbox(
            top_window_parameters_frame,
            bottom_value=effect_parameters[i][1],
            top_value=effect_parameters[i][2],
        )

        # Positioning the created spinbox
        spinbox.grid(
            row=i,
            column=column + 1
        )

        # Adding a label to describe the spinbox
        spinbox_label = tk.Label(
            top_window_parameters_frame,
            text=effect_parameters[i - start_row][0]
        )

        # Positioning the spinbox label
        spinbox_label.grid(
            row=i,
            column=column,
            padx=10,
            pady=10,
        )

        # Adding a label to give the spinbox range to the user
        spinbox_range = tk.Label(
            top_window_parameters_frame,
            text=f"Range: {effect_parameters[i][1]} to {effect_parameters[i][2]}",
        )

        # Positioning the spinbox label
        spinbox_range.grid(
            row=i,
            column=column + 2,
            padx=10,
            pady=10,
        )

        # Adding the spinbox values and the effect name to the 'spinbox_values' list
        spinbox_values.append(spinbox)

    # Function that saves the current open effect's parameters
    def save_current_effect_parameters():
        values = [float(s.spinbox.get()) for s in spinbox_values]
        save_effect_parameters(effect_name, values)

    # Variable to hold the save button that is pressed to save
    # the current open effect's parameters
    save_button = tk.Button(
        top_window,
        text="Save Parameters",
        command=save_current_effect_parameters,
    )

    # Positioning the save button on the effect parameters top window
    save_button.grid(
        row=end_row,
        column=column,
        padx=10,
        pady=10,
    )
