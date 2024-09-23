import tkinter as tk

from GUI.Widgets.Buttons.Buttons_Template.main_button import MainButton

""""
The 'MainCheckbox' class is used to create an instance of a checkbox, that is going to be used as a template for other 
checkboxes.
In the __init__ method:
- 'parent' is a reference to the parent widget, where 'MainCheckbox' will be placed;
- 'callback' is a function to be called when the checkbox is toggled. It is None by default;
- '**kwargs' refers to any arguments to be passed on this widget. They can be optional parameters or attributes.
The value of the checkbox is going to hold a bool value, which will be used to determine if the checkbox is toggled. The 
checkbox value is updated automatically when the checkbox state changes.
An instance of the 'MainButton' class is created, that is disabled by default until the checkbox is toggled on. 
The assigned command is used to check whether the checkbox is toggled on/off.
The callback function will be called when the checkbox is toggled, returning it's current status.
The 'checkbox_is_toggled' function is used to get the current status of the checkbox and return it.

The 'MainCheckboxFunctionality' class holds the 'track_checkbox_status_change' function.
The 'track_checkbox_status_change' function is used to enable/disable the 'MainButton' depending on state of the 
checkbox. If checkbox is toggled ON the button is enabled, and when the checkbox is toggled OFF, the button is disabled.
"""


class MainCheckbox(tk.Checkbutton):
    def __init__(self, parent, callback=None, **kwargs):
        super().__init__(parent, command=self.checkbox_is_toggled, **kwargs)
        self.value = tk.BooleanVar()

        self.configure(variable=self.value)

        self.button = MainButton(parent, text="Set Parameters", state=tk.DISABLED)

        self.command = self.checkbox_is_toggled

        self.callback = callback

        self.grid(sticky='W', padx=10, pady=10,)

    def checkbox_is_toggled(self):
        if self.callback:
            self.callback(self.value.get(), self.button)
            return self.value.get()


class MainCheckboxFunctionality:
    @staticmethod
    def track_checkbox_status_change(is_checked, button):
        button.config(state=tk.NORMAL if is_checked else tk.DISABLED)
