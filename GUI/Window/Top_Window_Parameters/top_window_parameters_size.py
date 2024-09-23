import platform

"""
The 'define_main_window_size' function is used to define the size and parameters for the  Top Window for effect
parameters. It sets the initial window width and height, calculates how to position it in the middle of the user's
screen and makes it non-resizable.
"""


def define_top_window_size(self):
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()

    window_width = None
    window_height = None

    if platform.system() == "Linux":
        window_width = int(screen_width * 0.25)
        window_height = int(screen_height * 0.40)
    elif platform.system() == "Windows":
        window_width = int(screen_width * 0.20)
        window_height = int(screen_height * 0.35)


    position_top = int(self.winfo_screenheight() / 2 - window_height / 2)
    position_right = int(self.winfo_screenwidth() / 2 - window_width / 2)

    self.geometry("%dx%d+%d+%d" % (window_width, window_height, position_right, position_top))

    self.resizable(False, False)
