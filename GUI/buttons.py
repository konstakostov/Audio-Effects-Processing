import tkinter as tk


class MainButton(tk.Button):
    def __init__(self, parent, callback=None, **kwargs):
        super().__init__(parent, command=self.button_is_toggled, **kwargs)

        # Create a Bool Tkinter value
        self.value = tk.BooleanVar()

        self.command = self.button_is_toggled

        self.callback = callback

        self.grid(sticky='W', padx=10, pady=10, )

    def button_is_toggled(self):
        # Disable button if checkbox is unchecked
        if self.callback:
            self.callback(self.value.get())
            self.configure(state=tk.DISABLED)
        # Enable button if checkbox is checked
        else:
            self.configure(state=tk.NORMAL)
