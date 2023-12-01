import tkinter as tk

root = tk.Tk()

input_field = tk.Entry(root, bg='yellow', fg='blue', width=15, show="*", font=("Helvetica", 16))
input_field.grid(column=1)

label = tk.Label(text="dfghjkl;")
label.grid(column=0)

root.mainloop()
