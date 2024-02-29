import tkinter as tk


class MainCheckboxFunctionality:
    # Static method, which checks the state of the checkbox.
    # When the checkbox is toggled ON the button is ENABLED.
    # When the checkbox is toggled OFF the button is DISABLED.
    @staticmethod
    def track_checkbox_status_change(is_checked, button):
        button.config(state=tk.NORMAL if is_checked else tk.DISABLED)
