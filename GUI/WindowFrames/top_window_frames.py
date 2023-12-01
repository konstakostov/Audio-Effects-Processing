import tkinter as tk

from GUI.WindowWidgets.entry_fields import TopEntryField


# entry_field_labels, entry_field_bottom_value, entry_field_top_value
def top_window_frames(self, start_row, end_row, column, entry_field_data):
    # A frame is created to store the layer and min size is set for it
    main_frame = tk.Frame()
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid(sticky='EW')

    for i in range(start_row, end_row):
        main_frame.grid_rowconfigure(i, weight=1, pad=10)

        entry_field = TopEntryField(
            self,
            bottom_value=entry_field_data[i][1],
            top_value=entry_field_data[i][2]
        )

        entry_field.grid(
            row=i,
            column=column,
        )

        entry_field_label = tk.Label(
            self,
            text=entry_field_data[i - start_row][0],
        )

        entry_field_label.grid(
            row=i,
            column=column + 1,
            padx=10,
            pady=10,
        )
