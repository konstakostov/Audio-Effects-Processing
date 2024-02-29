from tkinter import messagebox

from pedalboard import Pedalboard
from pedalboard.io import AudioFile

from Effects.determine_processed_wav_file_name import determine_output_file_name


def create_virtual_pedalboard(audio_effects, a_path):
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


