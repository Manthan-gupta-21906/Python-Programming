'''PanedWindow
The PanedWindow widget is a container that holds multiple widgets in resizable panes. Below is the syntax:

paned = PanedWindow(master, option=value)'''

from tkinter import *

root = Tk()
root.title("PanedWindow Example")

paned_main = PanedWindow(root, orient=HORIZONTAL)
paned_main.pack(fill=BOTH, expand=1)

entry = Entry(paned_main, bd=5)
paned_main.add(entry)

paned_vertical = PanedWindow(paned_main, orient=VERTICAL)
paned_main.add(paned_vertical)

scale = Scale(paned_vertical, orient=HORIZONTAL)
paned_vertical.add(scale)

root.mainloop()

'''Explanation:

PanedWindow(): Creates a resizable container.
add(): Adds widgets to panes.
orient: Controls horizontal or vertical layout.
Allows flexible and adjustable UI layouts.'''