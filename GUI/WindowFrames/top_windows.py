import tkinter as tk

from GUI.Effects.effect_parameters import Effects
from GUI.WindowFrames.top_window_frames import top_window_frames


class SecondaryWindow:
    @staticmethod
    def secondary_window(effect_name):
        top_window = tk.Toplevel()

        # Sets window title
        top_window.title(effect_name + " Parameters")

        # Sets initial size to 50% of screen size
        window_width = top_window.winfo_screenwidth() * 0.25
        window_height = top_window.winfo_screenheight() * 0.25

        # Center window on Users screen
        position_top = int(top_window.winfo_screenheight() / 2 - window_height / 2)
        position_right = int(top_window.winfo_screenwidth() / 2 - window_width / 2)

        top_window.geometry("%dx%d+%d+%d" % (window_width, window_height, position_right, position_top))

        # Makes window non-resizable
        top_window.resizable(False, False)

        for effect, parameters in Effects.used_effects.items():
            if effect == effect_name:
                top_window_frames(
                    top_window,
                    0,
                    len(parameters),
                    0,
                    parameters,
                )
