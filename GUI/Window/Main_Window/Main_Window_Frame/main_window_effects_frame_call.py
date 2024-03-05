from GUI.Window.Main_Window.Main_Window_Frame.main_window_effects_frame_creation import create_main_window_effect_frame

"""
The 'call_main_window_effects_frames' function is used to call all the frames, used in the Main Window.
"""


def call_main_window_effects_frames(parent, frame_data):
    for data in frame_data:
        create_main_window_effect_frame(parent, data)
