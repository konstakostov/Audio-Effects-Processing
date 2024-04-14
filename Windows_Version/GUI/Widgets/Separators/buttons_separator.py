from tkinter import ttk

"""
The 'create_button_separator' function creates a separator that is used to separate the processing and 
visualising sections of the GUI.
"""


def create_button_separator(self):
    button_separator = ttk.Separator(self, orient='horizontal', )
    button_separator.grid(
        row=10,
        column=0,
        columnspan=4,
        sticky='EW',
        padx=10,
        pady=10,
    )
