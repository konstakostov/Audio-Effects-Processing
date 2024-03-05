import tkinter as tk

"""
The 'MainSpinbox' class is used to create an instance of a spinbox, that is going to be used as a template for other 
spinboxes.
In the __init__ method:
- 'parent' is a reference to the parent widget, where 'MainSpinbox' will be placed;
- 'bottom_value' is a reference to the bottom value of the spinbox;
- 'top_value' is a reference to the top value of the spinbox;
- '**kwargs' refers to any arguments to be passed on this widget. They can be optional parameters or attributes.
The 'increment_value' variable is used to hold the increment value, which is used to determine how the values in the
spinbox change when the up/down buttons are pressed. The increment values is determined based on the bottom and top 
values of the spinbox.
The 'bottom_value' variable is used to hold the bottom value of the spinbox.
The 'top_value' variable is used to hold the top value of the spinbox.
The 'spinbox_validation' variable is used to hold the command, used for validating the characters, entered in the 
spinbox.
The 'validate_spinbox' function is used to validate the entered values in the spinbox. If the values are float or 
integer type it returns True and if they are not - it returns False, preventing the character to be entered in the 
spinbox.
"""


class MainSpinbox(tk.Entry):
    def __init__(self, parent, bottom_value, top_value, **kwargs):
        super().__init__(parent, **kwargs)

        # Variable to hold the increment value
        self.increment_value = None

        # Variables to hold top and bottom values of the entry field value range
        self.bottom_value = bottom_value
        self.top_value = top_value

        # Variable to hold the command, that validates the spinbox
        self.spinbox_validation = self.register(self.validate_spinbox)

        # Defining the value of the increment value,
        # based on the bottom and top value
        if top_value - bottom_value <= 5:
            increment_value = 0.1
        elif top_value - bottom_value <= 250:
            increment_value = 1
        elif top_value - bottom_value <= 500:
            increment_value = 10
        else:
            increment_value = 100

        # Variable to hold the spinbox widget,
        # and all it's parameters
        self.spinbox = tk.Spinbox(
            self,
            from_=bottom_value,
            to=top_value,
            increment=increment_value,
            validate='key',
            validatecommand=(self.spinbox_validation, '%P'),
        )

        # Assigning positioning details to every spinbox
        self.spinbox.grid(
            sticky="NSEW",
        )

    @staticmethod
    def validate_spinbox(value):
        try:
            float(value)
            return True

        except ValueError:
            return False
