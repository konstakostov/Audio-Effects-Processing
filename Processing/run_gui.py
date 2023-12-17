from GUI.main import MainWindow

# Running the GUI
# Making the window stay on screen until the user closes it.
# Without this the program will start and close, without the user noticing.
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
