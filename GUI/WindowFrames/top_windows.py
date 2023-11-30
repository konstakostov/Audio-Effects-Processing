import tkinter as tk


class SecondaryWindow:
    @staticmethod
    def secondary_window(window_title):
        top_window = tk.Toplevel()

        # Sets window title
        top_window.title(window_title + " Parameters")

        # Sets initial size to 50% of screen size
        window_width = top_window.winfo_screenwidth() * 0.4
        window_height = top_window.winfo_screenheight() * 0.25

        # Center window on Users screen
        position_top = int(top_window.winfo_screenheight() / 2 - window_height / 2)
        position_right = int(top_window.winfo_screenwidth() / 2 - window_width / 2)

        top_window.geometry("%dx%d+%d+%d" % (window_width, window_height, position_right, position_top))

        # Makes window non-resizable
        top_window.resizable(False, False)
