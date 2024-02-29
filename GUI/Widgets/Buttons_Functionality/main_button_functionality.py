from GUI.Window.Top_Window_Parameters.top_window_parameters import TopWindowSetEffectParameters


class MainButtonFunctionality:
    # The function calls the secondary_window function from 'top_windows.py'
    # It has one parameter 'effect_name', which determines for which effect the
    # Top Window is created for.
    @staticmethod
    def call_top_window_effects_parameters(effect_to_set_parameters):
        TopWindowSetEffectParameters.create_top_window_effect_parameters(effect_to_set_parameters)