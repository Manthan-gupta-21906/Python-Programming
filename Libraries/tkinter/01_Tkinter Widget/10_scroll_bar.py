'''The Scrollbar widget provides a scrolling mechanism for widgets such as Listbox, Text, or Canvas. It is used when the content is larger than the visible area. Below is the syntax:

scrollbar = tk.Scrollbar(master, option=value)'''

import tkinter as tk

root = tk.Tk()

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

mylist = tk.Listbox(root, yscrollcommand=scrollbar.set)

for line in range(100):
    mylist.insert(tk.END, "This is line number " + str(line))

mylist.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=mylist.yview)

root.mainloop()

'''A window appears with a scrollable list containing 100 items.
Explanation:

tk.Scrollbar(): Creates a vertical scrollbar.
yscrollcommand=scrollbar.set: Connects the listbox to the scrollbar.
scrollbar.config(command=mylist.yview): Enables scrolling behavior.
pack(side, fill): Positions the widgets correctly.'''