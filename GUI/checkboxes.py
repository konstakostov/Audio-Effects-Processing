import tkinter as tk

from GUI.validators import CheckboxValidator


class MainCheckbox(tk.Checkbutton):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, command=self.verify_checkbox, **kwargs)
        # Create a Bool Tkinter value
        self.value = tk.BooleanVar()

        # self.value is bound to the Checkbox value and updates
        # automatically when the Checkbox state changes
        self.configure(variable=self.value)

        # Assigns the function self.verify_checkbox as a command
        # for the checkbutton when it's activated/deactivated
        self.command = self.verify_checkbox

        # Widget is anchored to the left of the window (West) &
        # padding is set to 10 pixels (horizontal & vertical)
        self.pack(anchor=tk.W, padx=10, pady=10,)

    def verify_checkbox(self):
        if CheckboxValidator.is_checked(self.value):
            print("Checkbox is Checked!")
        else:
            print("Checkbox is not Checked!")
