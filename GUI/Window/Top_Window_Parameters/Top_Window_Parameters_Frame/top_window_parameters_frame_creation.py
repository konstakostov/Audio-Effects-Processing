import tkinter as tk

from GUI.Widgets.Spinboxes.main_spinbox import MainSpinbox
from GUI.Window.Top_Window_Parameters.Top_Window_Parameters_Functions.save_effect_parameters_function import save_effect_parameters

"""
The 'top_window_parameters_frame_creation' function is used to create a frame which holds widgets related to the 
parameters of the selected effect.
The 'top_window_parameters_frame' variable is used to create the frame and sets it's columns weight to 1.
The 'spinbox_values' variable is used to store all the spinbox values of the selected effect in a list.
After that we are iterating through all the rows, where each row corresponds to a specific effect parameter. Every row 
a 'MainSpinbox' class instance is used to create a spinbox which holds the value of the parameter, that will be defined 
by the user. 
The 'save_current_effect_parameters' function is used to create a button, that when pressed will save all the parameters
values from the 'spinbox_values' variable in the specific variable by calling the 'save_effect_parameters' function.
"""


def top_window_parameters_frame_creation(top_window, effect_name, start_row, end_row, column, effect_parameters):
    top_window_parameters_frame = tk.Frame(top_window)
    top_window_parameters_frame.grid_columnconfigure(0, weight=1)
    top_window_parameters_frame.grid(sticky='EW')

    spinbox_values = []

    for i in range(start_row, end_row):
        top_window_parameters_frame.grid_rowconfigure(i, weight=1, pad=10)

        spinbox = MainSpinbox(
            top_window_parameters_frame,
            bottom_value=effect_parameters[i][1],
            top_value=effect_parameters[i][2],
        )

        spinbox.grid(
            row=i,
            column=column + 1
        )

        spinbox_label = tk.Label(
            top_window_parameters_frame,
            text=effect_parameters[i - start_row][0]
        )

        spinbox_label.grid(
            row=i,
            column=column,
            padx=10,
            pady=10,
        )

        spinbox_range = tk.Label(
            top_window_parameters_frame,
            text=f"Range: {effect_parameters[i][1]} to {effect_parameters[i][2]}",
        )

        spinbox_range.grid(
            row=i,
            column=column + 2,
            padx=10,
            pady=10,
        )

        spinbox_values.append(spinbox)

    def save_current_effect_parameters():
        values = [float(s.spinbox.get()) for s in spinbox_values]
        save_effect_parameters(effect_name, values)

    save_button = tk.Button(
        top_window,
        text="Save Parameters",
        command=save_current_effect_parameters,
    )

    save_button.grid(
        row=end_row,
        column=column,
        padx=10,
        pady=10,
    )
