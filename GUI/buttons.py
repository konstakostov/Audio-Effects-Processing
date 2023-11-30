import tkinter as tk


class MainButton(tk.Button):
    def __init__(self, parent, text="", **kwargs):
        super().__init__(parent, text=text, **kwargs)

        # Create a Bool Tkinter value
        self.value = tk.BooleanVar()

        self.grid(sticky='EW', padx=10, pady=10,)
