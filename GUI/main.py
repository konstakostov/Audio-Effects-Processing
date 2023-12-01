import tkinter as tk

from GUI.WindowFrames.window_frames import main_frames


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Sets window title
        self.title("Audio Effects Processing")

        # Sets initial size to 50% of screen size
        window_width = self.winfo_screenwidth() * 0.5
        window_height = self.winfo_screenheight() * 0.5

        # Center window on Users screen
        position_top = int(self.winfo_screenheight() / 2 - window_height / 2)
        position_right = int(self.winfo_screenwidth() / 2 - window_width / 2)

        self.geometry("%dx%d+%d+%d" % (window_width, window_height, position_right, position_top))

        # Makes window resizable
        self.resizable(True, True)

        # Creates a list, containing effects name labels for 'Guitar Effects'
        guitar_effects = ['Chorus', 'Clipping', 'Distortion', 'Phaser']

        # Creates a list, containing effects name labels for 'Dynamic Range Effects'
        dynamic_range_effects = ['Compressor', 'Gain', 'Limiter']

        # First Frame. It will create 'Guitar Effects'
        # It takes start_row, end_row, column, frame_label, effects name labels as parameters
        main_frames(
            self,
            1,
            5,
            0,
            'Guitar-Style effects',
            guitar_effects
        )

        # Second Frame. It will create 'Dynamic Range Effects'
        # It takes start_row, end_row, column, frame_label, effects name labels as parameters
        main_frames(
            self,
            6,
            9,
            0,
            'Loudness and Dynamic Range Effects',
            dynamic_range_effects
        )


# Makes the window stay on screen until the user closes it.
# Without this the program will start and close, without the user noticing.
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
