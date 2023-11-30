import tkinter as tk


class MainCheckboxFunctions:
    # Static method, which checks the state of the checkbox.
    # When the checkbox is toggled ON the button is ENABLED.
    # When the checkbox is toggled OFF the button is DISABLED.
    @staticmethod
    def on_checkbox_change(is_checked, button):
        button.config(state=tk.NORMAL if is_checked else tk.DISABLED)
