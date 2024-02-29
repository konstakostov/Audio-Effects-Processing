def define_top_window_size(self):
    # Sets initial size to 50% of screen size
    window_width = self.winfo_screenwidth() * 0.20
    window_height = self.winfo_screenheight() * 0.35

    # Center window on Users screen
    position_top = int(self.winfo_screenheight() / 2 - window_height / 2)
    position_right = int(self.winfo_screenwidth() / 2 - window_width / 2)

    self.geometry("%dx%d+%d+%d" % (window_width, window_height, position_right, position_top))

    # Makes window non-resizable
    self.resizable(False, False)
