import tkinter as tk

from GUI.Widgets.Buttons_Functionality.main_button_functionality import MainButtonFunctionality
from GUI.Widgets.Checkboxes.main_checkbox import MainCheckbox
from GUI.Widgets.Checkboxes_Functionality.main_checkbox_functionality import MainCheckboxFunctionality


def create_main_window_effect_frame(parent, effects_input_data):
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

    # In the rows in range 'start_row' - 'end_row' are created checkboxes and buttons.
    # When the checkbox is activated, it enables the button.
    # The checkbox is positioned in column 'column', and the button in column 'column' + 1.
    for i in range(effects_input_data["start_row"], effects_input_data["end_row"]):
        main_window_frame.grid_rowconfigure(i, weight=1, pad=10)

        # Variable to hold the checkbox
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

        # Adding functionality to the checkbox button
        checkbox.button.config(
            command=lambda text=effects_input_data["effects_in_group"][i - effects_input_data["start_row"]]:
            MainButtonFunctionality.call_top_window_effects_parameters(text)
        )

