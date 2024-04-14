import tkinter as tk

from Windows_Version.GUI.Window.Main_Window.Main_Window_Processing.main_window_processing_frame_input_data import \
    MainWindowProcessingFrameInputData
from Windows_Version.GUI.Window.Main_Window.Main_Window_Visualisations.main_window_visualisation_frame import \
    create_main_window_visualisation_frame

from Windows_Version.GUI.Window.Main_Window.main_window_size import define_main_window_size
from Windows_Version.GUI.Widgets.Separators.processing_visualization_separator import create_processing_visualization_separator
from Windows_Version.GUI.Widgets.Separators.buttons_separator import create_button_separator

from Windows_Version.GUI.Window.Main_Window.Main_Window_Processing.main_window_processing_frame_call import \
    call_main_window_processing_frames

from Windows_Version.GUI.Widgets.Buttons.Buttons_Processing.choose_wav_file_button_to_process import \
    define_choose_wav_file_to_process_button
from Windows_Version.GUI.Widgets.Buttons.Buttons_Processing.process_wav_file_button import define_process_wav_file_button
from Windows_Version.GUI.Widgets.Buttons.Buttons_File_Explorer.open_last_selected_directory_button import \
    define_open_last_directory_button


"""
The 'MainWindow' class is used to call all the functions required to create the GUI.

The 'define_main_window_size' function is used to determine the size and properties of the created GUI window.

The 'create_processing_visualization_separator' function is used to create a separator to separate the processing and 
visualisation part of the GUI.

The 'create_button_separator' function is used to create a separator between the buttons for the processing part and the 
button to open the directory of the last chosen .wav file.

The 'call_main_window_processing_frames' function is used to call all the Processing Frames, displayed in the Main 
Window. 

The 'define_choose_wav_file_button' function is used to call the Button for choosing .wav file to process.

The 'define_process_wav_file_button' function is used to call the Button for processing the selected .wav file.

The 'define_open_last_directory_button' function is used to open the last selected input .wav file directory.

The 'create_main_window_visualisation_frame' function is used to call the Visualisation Frame, displayed in the Main 
Window. 
"""


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        define_main_window_size(self)

        create_processing_visualization_separator(self)

        create_button_separator(self)

        define_open_last_directory_button(self)

        call_main_window_processing_frames(self, MainWindowProcessingFrameInputData.effects_processing_input_data)

        define_choose_wav_file_to_process_button(self)

        define_process_wav_file_button(self)

        define_open_last_directory_button(self)

        create_main_window_visualisation_frame(self)
