'''The Label widget is used to display text or images in a Tkinter window. It is commonly used for showing messages, titles, or instructions. Below is the syntax:

label = tk.Label(master, option=value)

Parameter: master refers to the parent window or container in which the label is placed.

Example: This example creates a simple window and displays a text label.'''

import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="Manthan Gupta")
label.pack()

root.mainloop()

'''Explanation: label.pack() places the label inside the window.

Note: Tkinter widgets support many options such as font, bg (background) and fg (foreground). Only a few commonly used options are shown in the examples.'''