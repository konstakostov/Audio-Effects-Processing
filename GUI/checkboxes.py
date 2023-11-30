import tkinter as tk

from GUI.buttons import MainButton


class MainCheckbox(tk.Checkbutton):
    def __init__(self, parent, callback=None, **kwargs):
        super().__init__(parent, command=self.checkbox_is_toggled, **kwargs)
        # Create a Bool Tkinter value
        self.value = tk.BooleanVar()

        # self.value is bound to the Checkbox value and updates
        # automatically when the Checkbox state changes
        self.configure(variable=self.value)

        # Add MainButton as instance attribute
        self.button = MainButton(parent, text="Set Parameters", state=tk.DISABLED)

        # Assigns the function self.verify_checkbox as a command
        # for the checkbutton when it's activated/deactivated
        self.command = self.checkbox_is_toggled

        # Everytime the Checkbox is toggled it calls the 'checkbox_is_toggled'
        # is called and passes the current Checkbox status
        self.callback = callback

        # Widget is anchored to the left of the window (West) &
        # padding is set to 10 pixels (horizontal & vertical)
        self.grid(sticky='W', padx=10, pady=10,)

    # The function gets the current status of the checkbox and returns
    def checkbox_is_toggled(self):
        if self.callback:
            self.callback(self.value.get(), self.button)
            return self.value.get()
