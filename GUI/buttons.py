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
