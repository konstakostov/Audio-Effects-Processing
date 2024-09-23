import tkinter as tk

from GUI.Window.Top_Window_Parameters.top_window_parameters import TopWindowSetProcessingParameters

""""
The 'MainButton' class is used to create an instance of a button, that is going to be used as a template for other 
buttons.
In the __init__ method:
- 'parent' is a reference to the parent widget, where 'MainCheckbox' will be placed;
- 'text' provides text to the button, by default is None and no text will be placed in the button;
- '**kwargs' refers to any arguments to be passed on this widget. They can be optional parameters or attributes.
The value of the button is going to hold a bool value, which will be used to determine if the button is being pressed.

The 'MainButtonFunctionality' class is used to give functionality to the template button.
When the button is pressed is going to open a Top Window. The Top Window will allow the user to assign values to each of
the selected effect's parameters. 
"""


class MainButton(tk.Button):
    def __init__(self, parent, text="", **kwargs):
        super().__init__(parent, text=text, **kwargs)
        self.value = tk.BooleanVar()

        self.grid(sticky='EW', padx=10, pady=10,)


class MainButtonFunctionality:
    @staticmethod
    def call_top_window_effects_parameters(effect_to_set_parameters):
        TopWindowSetProcessingParameters.create_top_window_effect_parameters(effect_to_set_parameters)
