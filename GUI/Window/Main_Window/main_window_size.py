"""
The 'define_main_window_size' function is used to define the Main Window size and parameters.
It sets the Main Window title, the initial window width and height,calculates how to position it in the middle of the
user's screen and makes it resizable.
"""


def define_main_window_size(self):
    self.title("Audio Effects Buttons_Processing")

    window_width = self.winfo_screenwidth() * 0.40
    window_height = self.winfo_screenheight() * 0.50

    position_top = int(self.winfo_screenheight() / 2 - window_height / 2)
    position_right = int(self.winfo_screenwidth() / 2 - window_width / 2)

    self.geometry("%dx%d+%d+%d" % (window_width, window_height, position_right, position_top))

    self.resizable(True, True)
