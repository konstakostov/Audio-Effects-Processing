import tkinter as tk


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
