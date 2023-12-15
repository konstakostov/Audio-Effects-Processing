import tkinter as tk

from GUI.WindowWidgets.spinboxes import TopSpinbox


# entry_field_labels, entry_field_bottom_value, entry_field_top_value
def top_window_frames(self, start_row, end_row, column, entry_field_data):
    # A frame is created to store the layer and min size is set for it
    main_frame = tk.Frame()
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid(sticky='EW')

    for i in range(start_row, end_row):
        main_frame.grid_rowconfigure(i, weight=1, pad=10)

        default_spinbox_value = tk.StringVar()

        spinbox = TopSpinbox(
            self,
            bottom_value=entry_field_data[i][1],
            top_value=entry_field_data[i][2],
            textvariable=default_spinbox_value
        )

        spinbox.grid(
            row=i,
            column=column + 1,
        )

        spinbox_name = tk.Label(
            self,
            text=entry_field_data[i - start_row][0],
        )

        spinbox_name.grid(
            row=i,
            column=column,
            padx=10,
            pady=10,
        )

        spinbox_range = tk.Label(
            self,
            text=f"Range: {entry_field_data[i][1]} to {entry_field_data[i][2]}",
        )

        spinbox_range.grid(
            row=i,
            column=column + 2,
            padx=10,
            pady=10,
        )
