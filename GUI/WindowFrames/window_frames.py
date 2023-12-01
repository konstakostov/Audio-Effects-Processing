from GUI.WindowWidgets.checkboxes import MainCheckbox
import tkinter as tk

from GUI.WidgetFunctions.functions_buttons import MainButtonFunctions
from GUI.WidgetFunctions.functions_checkboxes import MainCheckboxFunctions


def main_frames(self, start_row, end_row, column, frame_label, checkbox_labels):
    # A frame is created to store the layer and min size is set for it
    main_frame = tk.Frame()
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid(sticky='EW')

    # A label to visualise the frame's effects, and it's positioned in the window.
    tk.Label(
        self,
        text=frame_label,
    ).grid(
        row=start_row - 1,
        column=column,
        padx=10,
        pady=10,
        sticky='EW'
    )

    # In the rows in range 'start_row' - 'end_row' are created checkboxes and buttons.
    # When the checkbox is activated, it enables the button.
    # The checkbox is positioned in column 'column', and the button in column 'column' + 1.
    for i in range(start_row, end_row):
        main_frame.grid_rowconfigure(i, weight=1, pad=10)

        checkbox = MainCheckbox(
            self,
            text=checkbox_labels[i - start_row],
            callback=MainCheckboxFunctions.on_checkbox_change,
        )

        checkbox.grid(
            row=i,
            column=column,
        )

        checkbox.button.grid(
            row=i,
            column=column + 1,
            padx=10,
            pady=10,
        )

        checkbox.button.config(
            command=lambda text=checkbox_labels[i - start_row]:
            MainButtonFunctions.set_parameters_button(text)
        )
