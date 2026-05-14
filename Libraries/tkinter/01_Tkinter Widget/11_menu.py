'''The Menu widget is used to create menu bars and dropdown menus in a Tkinter application. Below is the syntax:

menu = tk.Menu(master, option=value)'''

import tkinter as tk

root = tk.Tk()

menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")

root.mainloop()

'''Explanation:

tk.Menu(): Creates a menu container.
add_cascade(): Adds dropdown menus to the menu bar.
add_command(): Adds menu items.
add_separator(): Adds a dividing line.
root.config(menu=menu): Attaches the menu bar to the window.'''