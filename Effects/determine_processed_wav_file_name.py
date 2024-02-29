# Function to determine the output audio file name
import os


def determine_output_file_name(file_path):
    # Variables to hold the file directory and the file name with its extension
    directory, file = os.path.split(file_path)
    # Variables to hold the file name and file extension
    file_name, file_extension = os.path.splitext(file)

    # Variable to hold the initial output file name
    output_name = f"{file_name}_output_1{file_extension}"

    # Counter to add to the output file nae
    counter = 2

    # # Modifying the output file name if
    # a file with the same name exists
    while os.path.exists(os.path.join(directory, output_name)):
        output_name = f"{file_name}_output_{counter}{file_extension}"
        counter += 1

    output_file = os.path.join(directory, output_name)

    # Returning the output file name
    return output_file
