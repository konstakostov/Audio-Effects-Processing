import tkinter as tk

from Effects.Effects_Data.audio_effects_groups_data import AudioEffectsGroupsData
from GUI.Window.Top_Window_Parameters.Top_Window_Parameters_Frame.top_window_parameters_frame_creation import top_window_parameters_frame_creation
from GUI.Window.Top_Window_Parameters.top_window_parameters_size import define_top_window_size

"""
The 'TopWindowSetProcessingParameters' class holds the 'create_top_window_effect_parameters' function.
The 'create_top_window_effect_parameters' function is used to create a Top Window, that displays the selected effect
parameters, the Top Window title and creates the frame used to position the items in the Top Window.
"""


class TopWindowSetProcessingParameters:
    @staticmethod
    def create_top_window_effect_parameters(effect_name_to_set_parameters):
        top_window_effect_parameters = tk.Toplevel()

        top_window_effect_parameters.title(effect_name_to_set_parameters + " Parameters")

        define_top_window_size(top_window_effect_parameters)

        for effect_group, effects in AudioEffectsGroupsData.effects_by_groups.items():
            for effect, parameters in effects.items():
                if effect == effect_name_to_set_parameters:
                    top_window_parameters_frame_creation(
                        top_window_effect_parameters,
                        effect,
                        0,
                        len(parameters),
                        0,
                        parameters,
                    )
