from tkinter import ttk

"""
The 'create_processing_visualization_separator' function creates a separator that is used to separate the buttons for 
the processing part of the GUI and the button to open the directory of the last chosen .wav file.
"""


def create_processing_visualization_separator(self):
    processing_visualization_separator = ttk.Separator(self, orient='vertical', )
    processing_visualization_separator.grid(
        row=0,
        column=4,
        rowspan=12,
        sticky='NS',
        padx=10,
        pady=10,
    )
