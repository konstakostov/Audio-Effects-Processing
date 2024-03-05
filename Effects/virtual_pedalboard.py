from tkinter import messagebox

from pedalboard import Pedalboard
from pedalboard.io import AudioFile

from Effects.Effects_Essential_Processes.determine_processed_wav_file_name import determine_output_file_name

"""
This function is used to create the Virtual Pedalboard. 
The 'board' variable is used to hold the Pedalboard object.
The 'output_name' variable is used to hold and determine the output file name.
The input audio file is opened, read and processed into chunks for faster processing time.
After successfully processing the input file a message is returned to the user notifying them the process is completed.
"""


def create_virtual_pedalboard(audio_effects, a_path):
    board = Pedalboard(audio_effects)

    output_name = determine_output_file_name(a_path)

    with AudioFile(a_path) as file:
        with AudioFile(output_name, "w", file.samplerate, file.num_channels) as output:
            while file.tell() < file.frames:
                chunk = file.read(int(file.samplerate))

                board_processed = board(chunk, file.samplerate, reset=False)
                output.write(board_processed)

    return messagebox.showinfo(
        "Processing Status",
        "Audio Processing Completed!")
