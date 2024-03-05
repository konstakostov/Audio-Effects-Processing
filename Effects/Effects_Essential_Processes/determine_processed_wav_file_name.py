import os

"""
This function is used to determine the output file name.
The 'directory' and 'file' variables store the current file directory and file name and extension.
The 'file_name' and 'file_extension' variables store the file name and it's extension.
The 'output_name' variables store the initial output file name.
A check is performed on the output file name to determine if file with this name exists in the directory.
If such file does exist then the counter is increased by 1 and the check is performed again until a unique file name 
is created.
When the final output file name is created is returned when the function is called.
"""


def determine_output_file_name(file_path):
    directory, file = os.path.split(file_path)
    file_name, file_extension = os.path.splitext(file)

    output_name = f"{file_name}_output_1{file_extension}"

    counter = 2

    while os.path.exists(os.path.join(directory, output_name)):
        output_name = f"{file_name}_output_{counter}{file_extension}"
        counter += 1

    output_file = os.path.join(directory, output_name)

    return output_file
