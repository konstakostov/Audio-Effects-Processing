import tkinter as tk

from GUI.checkboxes import MainCheckbox


class App(tk.Tk):
    def __init__(self):
        super().__init__()

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

        self.checkbox = MainCheckbox(self, text="Checkboxes")


if __name__ == "__main__":
    app = App()
    app.mainloop()
