from GUI.WindowWidgets.checkboxes import MainCheckbox
import tkinter as tk

from GUI.WidgetFunctions.functions_buttons import MainButtonFunctions
from GUI.WidgetFunctions.functions_checkbox import MainCheckboxFunctions


# Second layer. It will store 'Dynamic Range Effects'
def second_layer(self):
    # A frame is created to store the layer and min size is set for it
    frame = tk.Frame(self)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid(sticky='EW')

    # A label to visualise the frame's effects, and it's positioned in the window.
    tk.Label(
        self,
        text="Dynamic Range Effects"
    ).grid(
        row=5,
        column=0,
        padx=10,
        pady=10,
        sticky='EW',
    )

    # In the rows in range 1-4 are created checkboxes and buttons.
    # When the checkbox is activated, it enables the button.
    # The checkbox is positioned in column 0, and the button in column 1.
    for i in range(6, 9):
        frame.grid_rowconfigure(i, weight=1, pad=10)

        checkboxes = MainCheckbox(
            self,
            text=(
                "Compressor" if i == 6 else
                "Gain" if i == 7 else
                "Limiter"),
            callback=MainCheckboxFunctions.on_checkbox_change,
        )

        checkboxes.grid(
            row=i,
            column=0,
        )

        checkboxes.button.grid(
            row=i,
            column=1,
            padx=10,
            pady=10,
        )

        checkboxes.button.config(
            command=lambda text=checkboxes.cget("text"):
            MainButtonFunctions.set_parameters_button(text)
        )
