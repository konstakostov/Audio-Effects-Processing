import tkinter as tk
from tkinter import messagebox


class TopEntryField(tk.Entry):
    def __init__(self, parent, bottom_value, top_value, **kwargs):
        super().__init__(parent, **kwargs)

        self.bottom_value = bottom_value
        self.top_value = top_value

        validation_command = (self.register(self.validate_entry_field), "%P")

        self.config(
            validate="all",
            validatecommand=validation_command
        )

        self.grid(
            sticky="NSEW",
            padx=10,
            pady=10,
        )

    @staticmethod
    def validate_entry_field(self, value):
        try:
            if self.bottom_value <= value <= self.top_value:
                return True
            else:
                messagebox.showerror(
                    "Invalid input",
                    f"The number must be between {self.bottom_value} and {self.top_value}")
                return False
        except ValueError:
            messagebox.showerror(
                "Invalid input",
                f"The input must be a number in the range {self.bottom_value} - {self.top_value}")
            return False
