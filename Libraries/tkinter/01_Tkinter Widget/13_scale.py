'''The Scale widget provides a graphical slider that allows users to select a numeric value from a given range. Below is the syntax:

scale = Scale(master, from_=min, to=max, orient=VERTICAL | HORIZONTAL)'''

from tkinter import *

master = Tk()

# Vertical scale
vertical_scale = Scale(master, from_=0, to=42)
vertical_scale.pack()

# Horizontal scale
horizontal_scale = Scale(master, from_=0, to=200, orient=HORIZONTAL)
horizontal_scale.pack()

master.mainloop()

'''Explanation:

Scale(): Creates a slider widget.
from_ / to: Defines the range of values.
orient: Sets slider direction (VERTICAL or HORIZONTAL).
pack(): Places the widget in the window.'''