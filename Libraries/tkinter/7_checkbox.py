'''The Checkbutton widget is used to create a checkbox that can be toggled on or off. It is usually linked to a variable to store its current state. Below is the syntax:

check = tk.Checkbutton(master, option=value)'''

import tkinter as tk

root = tk.Tk()

var1 = tk.IntVar()
var2 = tk.IntVar()

tk.Checkbutton(root, text="Male", variable=var1).grid(row=0, sticky=tk.W)
tk.Checkbutton(root, text="Female", variable=var2).grid(row=1, sticky=tk.W)

root.mainloop()


'''Explanation:

tk.IntVar(): Stores the checkbox state (1 or 0).
grid(): Aligns widgets in rows and columns.
sticky=tk.W: Aligns the checkbox to the left.'''