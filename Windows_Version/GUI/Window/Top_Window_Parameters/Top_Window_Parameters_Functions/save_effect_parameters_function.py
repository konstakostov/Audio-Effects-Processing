from Windows_Version.GUI.Variables.stored_variables import VariableStorage

"""
The 'save_effect_parameters' function is used to save the effect parameter value when the specific button to save them 
is pressed.
"""


def save_effect_parameters(effect_name, values):
    VariableStorage.saved_effect_parameters[effect_name] = values
