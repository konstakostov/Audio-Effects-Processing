from GUI.Window.Main_Window.Main_Window_Processing.main_window_processing_frame_creation import create_main_window_processing_frame

"""
The 'call_main_window_effects_frames' function is used to call all the frames, used in the Main Window.
"""


def call_main_window_processing_frames(parent, frame_data):
    for data in frame_data:
        create_main_window_processing_frame(parent, data)
