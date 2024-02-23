import os
from tkinter import messagebox

from pedalboard import Pedalboard
from pedalboard.io import AudioFile


def process_audio(audio_effects, a_path):
    # Variable to hold the Pedalboard object
    board = Pedalboard(audio_effects)

    # Variable to hold and determine and the output file name
    output_name = determine_output_file_name(a_path)

    # Opening the input file with AudioFile
    with AudioFile(a_path) as file:
        # Creating the output file with the AudioFile
        with AudioFile(output_name, "w", file.samplerate, file.num_channels) as output:
            # The input file is split into chunks, so it is easier and faster to process it
            # Each chunk is then written in the 'output' file, until the whole input file is processed
            while file.tell() < file.frames:
                chunk = file.read(int(file.samplerate))

                board_processed = board(chunk, file.samplerate, reset=False)
                output.write(board_processed)

    # Returning a message to the user when the processing is completed
    return messagebox.showinfo(
        "Processing Status",
        "Audio Processing Completed!")


# Function to determine the output audio file name
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
