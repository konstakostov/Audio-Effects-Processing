from GUI.Variables.stored_variables import VariableStorage


# Function that saves the effect parameter value when the button is pressed
def save_effect_parameters(effect_name, values):
    VariableStorage.saved_effect_parameters[effect_name] = values
