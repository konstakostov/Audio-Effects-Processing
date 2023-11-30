import tkinter as tk

from GUI.WindowFrames.window_second_layer import second_layer
from GUI.WindowFrames.window_first_layer import first_layer


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

        # Calls all the different layers.
        # Each layer contains different effects
        first_layer(self)
        second_layer(self)


# Makes the window stay on screen until the user closes it.
# Without this the program will start and close, without the user noticing.
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
