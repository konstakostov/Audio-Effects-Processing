import tkinter as tk

from GUI.buttons import MainButton
from GUI.checkboxes import MainCheckbox


class App(tk.Tk):
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

        self.first_layer()
        self.second_layer()

    def first_layer(self):
        frame = tk.Frame(self)

        frame.grid(sticky='EWNS')
        for i in range(5):
            frame.grid_rowconfigure(i, weight=1, pad=10)
        frame.grid_columnconfigure(0, weight=1)

        tk.Label(
            self,
            text="Guitar Effects"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky='EW',
        )

        MainCheckbox(
            self,
            text="Chorus",
            callback=self.on_checkbox_change,
        ).grid(
            row=1,
            column=0
        )

        button = MainButton(
            self,
            text="Example",
            state=tk.DISABLED,
        )
        button.grid(
            row=1,
            column=1,
        )

        MainCheckbox(
            self,
            text="Clipping",
            callback=self.on_checkbox_change,
        ).grid(
            row=2,
            column=0
        )

        MainCheckbox(
            self,
            text="Distortion",
            callback=self.on_checkbox_change,
        ).grid(
            row=3,
            column=0
        )

        MainCheckbox(
            self,
            text="Phaser",
            callback=self.on_checkbox_change,
        ).grid(
            row=4,
            column=0,
        )

    def second_layer(self):
        frame = tk.Frame(self)

        frame.grid(sticky='EW')
        for i in range(4):
            frame.grid_rowconfigure(i, weight=1)

        frame.grid_columnconfigure(0, weight=1)

        tk.Label(
            self,
            text="Dynamic Range Effects"
        ).grid(
            row=5,
            column=0,
            padx=10,
            pady=10,
            sticky='EW',
        )

        MainCheckbox(
            self,
            text="Compressor",
            callback=self.on_checkbox_change,
        ).grid(
            row=6,
            column=0
        )

        MainCheckbox(
            self,
            text="Gain",
            callback=self.on_checkbox_change,
        ).grid(
            row=7,
            column=0
        )

        MainCheckbox(
            self,
            text="Limiter",
            callback=self.on_checkbox_change,
        ).grid(
            row=8,
            column=0
        )

    @staticmethod
    def on_checkbox_change(is_checked, button):
        button.update_state(is_checked)


if __name__ == "__main__":
    app = App()
    app.mainloop()
