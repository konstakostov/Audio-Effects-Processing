import tkinter as tk

from GUI.Widgets.Buttons.choose_wav_file_button import define_choose_wav_file_button
from GUI.Widgets.Buttons.process_wav_file_button import define_process_wav_file_button
from GUI.Window.Main_Window.main_window_effects_frame_call import call_main_window_effects_frames
from GUI.Window.Main_Window.main_window_effects_frame_input_data import MainWindowEffectsFrameInputData
from GUI.Window.Main_Window.main_window_size import define_main_window_size


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        define_main_window_size(self)

        call_main_window_effects_frames(self, MainWindowEffectsFrameInputData.effects_frames_input_data)

        define_choose_wav_file_button(self)

        define_process_wav_file_button(self)


