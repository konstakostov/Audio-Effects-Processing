import tkinter as tk

# Notes for the __init__ method:
# 'parent' is a reference to the parent widget, where 'MainCheckbox' will be placed, in this case 'App'.
# 'bottom_value' and 'top_value' define the range of the value that can be entered in the entry field
# '**kwargs' refers to any arguments to be passed on this widget. They can be optional
# parameters or attributes (text/font/etc.)


class TopEntryField(tk.Entry):
    def __init__(self, parent, bottom_value, top_value, **kwargs):
        super().__init__(parent, **kwargs)

        # Variables to hold top and bottom values of the entry field value range
        self.bottom_value = bottom_value
        self.top_value = top_value

        # Variable to hold the error label, that displays errors if they occur
        self.error_label = tk.Label(self.master)

        # Variable to hold the command, that validates each entry field
        # "%P" represents the value of the entry widget if an edit occurs (if editing is allowed)
        validation_command = (self.register(self.validate_entry_field), "%P")

        # Validation occurs whenever there is a change in the entry field's input
        # 'validation_command' is assigned as the validating function
        self.config(
            validate="all",
            validatecommand=validation_command
        )

        # Assigning positioning details to every entry field
        self.grid(
            sticky="NSEW",
            padx=10,
            pady=10,
        )

        # Positioning the error label at the last row and
        # assigning positioning details to it
        self.error_label.grid(
            row=99,
            column=0,
            sticky="SEW",
            padx=5,
            pady=5,
        )

    # Validating function of every entry field
    def validate_entry_field(self, value: str):
        # Checking if the selected entry field value is:
        #   - Empty
        #   - OR Every character is digit or '.'
        #   - AND Only 1 or less '.' characters occur
        #   - AND The value is in predefined range

        self.config(validatecommand=(self.register(self.validate_entry_field), "%P"))

        if not value:
            self.error_label.config(text="", fg="black")
            return True

        if all(c.isdigit() or (c == '.') for c in value) and value.count('.') <= 1:
            try:
                value_as_float = float(value)
                if self.bottom_value <= value_as_float <= self.top_value:
                    self.error_label.config(text="", fg="black")
                    return True
                else:
                    raise ValueError

            except ValueError:
                self.error_label.config(
                    text=f"The number must be between {self.bottom_value} and {self.top_value}",
                    fg="red",
                    font=('Segoe UI', '10', 'bold',),
                )
                return False

        else:
            self.error_label.config(
                text="Entered value must be a number",
                fg="red",
                font=('Segoe UI', '10', 'bold',),
            )
            return False
