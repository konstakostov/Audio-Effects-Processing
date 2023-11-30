import tkinter as tk

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

        # Calls all the different layers.
        # Each layer contains different effects
        self.first_layer()
        self.second_layer()

    def first_layer(self):
        frame = tk.Frame(self)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid(sticky='EWNS')

        tk.Label(
            self,
            text="Guitar Effects",
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky='EW',
        )

        for i in range(1, 5):
            frame.grid_rowconfigure(i, weight=1, pad=10)

            checkboxes = MainCheckbox(
                self,
                text=(
                    "Chorus" if i == 1 else
                    "Clipping" if i == 2 else
                    "Distortion" if i == 3 else
                    "Phaser"),
                callback=self.on_checkbox_change,
            )
            checkboxes.grid(
                row=i,
                column=0,
            )

            checkboxes.button.grid(
                row=i,
                column=1,
                padx=10,
                pady=10,
                sticky='EW',
            )

    def second_layer(self):
        frame = tk.Frame(self)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid(sticky='EW')

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

        for i in range(6, 9):
            frame.grid_rowconfigure(i, weight=1, pad=10)

            checkboxes = MainCheckbox(
                self,
                text=(
                    "Compressor" if i == 6 else
                    "Gain" if i == 7 else
                    "Limiter"),
                callback=self.on_checkbox_change,
            )

            checkboxes.grid(
                row=i,
                column=0,
            )

            checkboxes.button.grid(
                row=i,
                column=1,
                padx=10,
                pady=10,
                # sticky='EW',
            )

    @staticmethod
    def on_checkbox_change(is_checked, button):
        button.config(state=tk.NORMAL if is_checked else tk.DISABLED)


if __name__ == "__main__":
    app = App()
    app.mainloop()
