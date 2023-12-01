import tkinter as tk

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

        # # 'rate_hz', 'depth', 'centre_delay_ms', 'feedback', 'mix'
        # chorus_parameters =
        #
        # # threshold_db
        # clipping_parameters = [
        #
        # ]

        used_effects = {
            'Chorus': [
                ['Rate [Hz]', 0, 1000],
                ['Depth', 0, 1],
                ['Centre Delay [ms]', 0, 1000],
                ['Feedback', 0, 1],
                ['Mix', 0, 1],
            ],
            'Clipping': [
                ['Threshold [dB]', -100, 100],
            ],
            'Distortion': [],
            'Phaser': [],
            'Compressor': [],
            'Gain': [],
            'Limiter': [],
        }

        for effect, parameters in used_effects.items():
            if effect == effect_name:
                top_window_frames(
                    top_window,
                    0,
                    len(parameters) - 1,
                    0,
                    parameters,
                )
