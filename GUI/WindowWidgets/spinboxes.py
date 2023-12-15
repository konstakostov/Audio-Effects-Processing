import tkinter as tk

# Notes for the __init__ method:
# 'parent' is a reference to the parent widget, where 'MainCheckbox' will be placed, in this case 'App'.
# 'bottom_value' and 'top_value' define the range of the value that can be entered in the entry field
# '**kwargs' refers to any arguments to be passed on this widget. They can be optional
# parameters or attributes (text/font/etc.)


class TopSpinbox(tk.Entry):
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
        if bottom_value == 0 and top_value == 1:
            increment_value = 0.1
        elif top_value - bottom_value <= 100:
            increment_value = 1
        else:
            increment_value = 10

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

    # Validating function of every spinbox
    # If the entered value is float or integer it returns True,
    # else it returns False and does not allow the char to be entered
    # in the spinbox
    @staticmethod
    def validate_spinbox(value):
        try:
            float(value)
            return True

        except ValueError:
            return False
