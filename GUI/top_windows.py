import tkinter as tk

from GUI.effects_data import TopWindowEffectsParameters
from GUI.widgets import TopSpinbox


# Top Window that displays effects parameters
class SecondaryWindow:
    # Dictionary to hold all the saved effect parameters
    saved_effect_parameters = {}

    # Function that creates the top window and positions it
    @staticmethod
    def secondary_window(effect_name):
        # Creating the top window
        top_window = tk.Toplevel()

        # Sets window title
        top_window.title(effect_name + " Parameters")

        # Sets initial size to 50% of screen size
        window_width = top_window.winfo_screenwidth() * 0.20
        window_height = top_window.winfo_screenheight() * 0.35

        # Center window on Users screen
        position_top = int(top_window.winfo_screenheight() / 2 - window_height / 2)
        position_right = int(top_window.winfo_screenwidth() / 2 - window_width / 2)

        top_window.geometry("%dx%d+%d+%d" % (window_width, window_height, position_right, position_top))

        # Makes window non-resizable
        top_window.resizable(False, False)

        # Iterating through every effect and it's parameters names, bottom/top values
        for effect, parameters in TopWindowEffectsParameters.used_effects.items():
            if effect == effect_name:
                top_window_frames(
                    top_window,
                    effect,
                    0,
                    len(parameters),
                    0,
                    parameters,
                )

    # Function that saves the effect parameter value when the button is pressed
    @staticmethod
    def save_parameters(effect_name, values):
        SecondaryWindow.saved_effect_parameters[effect_name] = values


def top_window_frames(top_window, effect_name, start_row, end_row, column, entry_field_data):
    # A frame is created to store the layer and min size is set for it
    main_frame = tk.Frame(top_window)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid(sticky='EW')

    # List for storing all current spinbox objects
    spinbox_values = []

    # Iterating through each row and the effect parameter that it corresponds to
    for i in range(start_row, end_row):
        main_frame.grid_rowconfigure(i, weight=1, pad=10)

        # Creating the spinbox and defining bottom and top value
        spinbox = TopSpinbox(
            main_frame,
            bottom_value=entry_field_data[i][1],
            top_value=entry_field_data[i][2],
        )

        # Positioning the created spinbox
        spinbox.grid(
            row=i,
            column=column + 1,
        )

        # Adding a label to describe the spinbox
        spinbox_name = tk.Label(
            main_frame,
            text=entry_field_data[i - start_row][0],
        )

        # Positioning the spinbox label
        spinbox_name.grid(
            row=i,
            column=column,
            padx=10,
            pady=10,
        )

        # Adding a label to give the spinbox range to the user
        spinbox_range = tk.Label(
            main_frame,
            text=f"Range: {entry_field_data[i][1]} to {entry_field_data[i][2]}",
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
    def save_parameters():
        values = [float(s.spinbox.get())for s in spinbox_values]
        SecondaryWindow.save_parameters(effect_name, values)

    # Variable to hold the save button that is pressed to save
    # the current open effect's parameters
    save_button = tk.Button(
        top_window,
        text="Save Parameters",
        command=save_parameters,
    )

    # Positioning the save button on the effect parameters top window
    save_button.grid(
        row=end_row,
        column=column,
        padx=10,
        pady=10,
    )
