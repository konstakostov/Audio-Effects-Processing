from GUI.Window.Main_Window.main_window_effects_frame_creation import create_main_window_effect_frame


def call_main_window_effects_frames(parent, frame_data):
    for data in frame_data:
        create_main_window_effect_frame(parent, data)
