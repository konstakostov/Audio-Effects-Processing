from GUI.WindowFrames.top_windows import SecondaryWindow


class MainButtonFunctions:
    # The function calls the secondary_window function from 'top_windows.py'
    # It has one parameter 'effect_name', which determines for which effect the
    # Top Window is created for.
    @staticmethod
    def set_parameters_button(effect_name):
        SecondaryWindow.secondary_window(effect_name)
