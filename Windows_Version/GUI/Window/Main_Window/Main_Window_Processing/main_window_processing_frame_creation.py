import tkinter as tk

from Windows_Version.GUI.Widgets.Buttons.Buttons_Template.main_button import MainButtonFunctionality
from Windows_Version.GUI.Widgets.Checkboxes.main_checkbox import MainCheckbox, MainCheckboxFunctionality

"""
The 'create_main_window_effect_frame' function is used to create each frame for the Main Window. The weight for each of 
columns in the frame is set to 1.
The label for each frame is the selected group name.
In each frame a checkboxes and buttons are created, which are positioned bellow the label using the 'MainCheckbox' class
as template. The number of checkboxes and buttons are determined by the number of effects in each group. The rows and 
columns they take in the Main Window are defined beforehand. The button, next to each checkbox, is used to call a Top
Window that allows the user to set the values of corresponding effect parameters.
"""


def create_main_window_processing_frame(parent, effects_input_data):
    main_window_frame = tk.Frame(parent)
    main_window_frame.grid_columnconfigure(0, weight=1)
    main_window_frame.grid(sticky="EW")

    tk.Label(
        parent,
        text=effects_input_data["effects_group_name"],
        font=('Segoe UI', '10', 'bold',),
    ).grid(
        row=effects_input_data["start_row"] - 1,
        column=effects_input_data["column"],
        padx=10,
        pady=10,
        sticky="W")

    for i in range(effects_input_data["start_row"], effects_input_data["end_row"]):
        main_window_frame.grid_rowconfigure(i, weight=1, pad=10)

        checkbox = MainCheckbox(
            parent,
            text=effects_input_data["effects_in_group"][i - effects_input_data["start_row"]],
            callback=MainCheckboxFunctionality.track_checkbox_status_change,
        )

        checkbox.grid(
            row=i,
            column=effects_input_data["column"]
        )

        checkbox.button.grid(
            row=i,
            column=effects_input_data["column"] + 1,
            padx=10,
            pady=10,
        )

        checkbox.button.config(
            command=lambda text=effects_input_data["effects_in_group"][i - effects_input_data["start_row"]]:
            MainButtonFunctionality.call_top_window_effects_parameters(text)
        )

