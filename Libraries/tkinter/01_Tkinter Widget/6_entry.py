''' The Entry widget is used to accept single-line text input from the user. For multi-line text input, the Text widget is used instead. Below is the syntax:

entry = tk.Entry(master, option=value) '''

import tkinter as tk

root = tk.Tk()

tk.Label(root, text="First Name").grid(row=0, column=0)
tk.Label(root, text="Last Name").grid(row=1, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)


entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

root.mainloop()

'''Explanation:

tk.Entry(): Creates a single-line text input box.
grid(): Arranges widgets in rows and columns.'''