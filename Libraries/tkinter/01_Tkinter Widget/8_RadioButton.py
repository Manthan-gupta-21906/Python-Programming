'''The Radiobutton widget allows the user to select exactly one option from a group of choices. All radio buttons in a group share the same variable. Below is the syntax:

radio = tk.Radiobutton(master, option=value)'''

import tkinter as tk

root = tk.Tk()
v = tk.IntVar()

tk.Radiobutton(root, text="A", variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(root, text="B", variable=v, value=2).pack(anchor=tk.W)
root.mainloop()

'''Explanation:

tk.Radiobutton(): Creates a radio button widget.
tk.IntVar(): Stores the selected option value.
value: Assigned value when the radio button is selected.
anchor=tk.W: Aligns buttons to the left.'''