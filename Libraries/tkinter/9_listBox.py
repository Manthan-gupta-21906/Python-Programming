'''The Listbox widget displays a list of items from which the user can select one or more options. Below is the syntax:

listbox = tk.Listbox(master, option=value)'''

import tkinter as tk

root = tk.Tk()

lb = tk.Listbox(root)
lb.insert(1, "Python")
lb.insert(2, "Java")
lb.insert(3, "C++")
lb.insert(4, "Any other")

lb.pack()
root.mainloop()

'''Explanation:

tk.Listbox(): Creates a list container.
insert(): Adds items to the listbox.
pack(): Displays the listbox in the window.'''