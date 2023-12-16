import tkinter as tk

# Notes for the __init__ method:
# 'parent' is a reference to the parent widget, where 'MainCheckbox' will be placed,
# in this case 'MainCheckbox'.
# 'text' provides text to the button, by default is None and no text will be placed in the button.
# '**kwargs' refers to any arguments to be passed on this widget. They can be optional
# parameters or attributes (text/font/etc.)


class MainButton(tk.Button):
    def __init__(self, parent, text="", **kwargs):
        super().__init__(parent, text=text, **kwargs)

        # Create a Bool Tkinter value
        self.value = tk.BooleanVar()

        # Widget is anchored to Left-Right of the window (East-West) &
        # padding is set to 10 pixels (horizontal & vertical)
        self.grid(sticky='EW', padx=10, pady=10,)


# Notes for the __init__ method:
# 'parent' is a reference to the parent widget, where 'MainCheckbox' will be placed, in this case 'App'.
# 'callback' is a function to be called when the checkbox is toggled. It is None by default,
# but accepts the current state of the checkbox and 'MainButton' instance.
# '**kwargs' refers to any arguments to be passed on this widget. They can be optional
# parameters or attributes (text/font/etc.)


class MainCheckbox(tk.Checkbutton):
    def __init__(self, parent, callback=None, **kwargs):
        super().__init__(parent, command=self.checkbox_is_toggled, **kwargs)
        # Create a Bool Tkinter value
        self.value = tk.BooleanVar()

        # self.value is bound to the Checkbox value and updates
        # automatically when the Checkbox state changes
        self.configure(variable=self.value)

        # Add MainButton as instance attribute, by default is disabled
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


# Notes for the __init__ method:
# 'parent' is a reference to the parent widget, where 'MainCheckbox' will be placed, in this case 'App'.
# 'bottom_value' and 'top_value' define the range of the value that can be entered in the spinbox
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


