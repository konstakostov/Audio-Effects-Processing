import tkinter as tk

from GUI.top_windows import SecondaryWindow


class MainButtonFunctions:
    # The function calls the secondary_window function from 'top_windows.py'
    # It has one parameter 'effect_name', which determines for which effect the
    # Top Window is created for.
    @staticmethod
    def set_parameters_button(effect_name):
        SecondaryWindow.secondary_window(effect_name)


class MainCheckboxFunctions:
    # Static method, which checks the state of the checkbox.
    # When the checkbox is toggled ON the button is ENABLED.
    # When the checkbox is toggled OFF the button is DISABLED.
    @staticmethod
    def on_checkbox_change(is_checked, button):
        button.config(state=tk.NORMAL if is_checked else tk.DISABLED)
