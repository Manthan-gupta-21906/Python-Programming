'''SpinBox
The Spinbox widget is an enhanced Entry widget that allows users to select a value from a fixed range using up and down arrows. Below is the syntax:

spinbox = Spinbox(master, option=value)'''

from tkinter import *

root = Tk()
root.title("Spinbox Example")

spinbox = Spinbox(root, from_=0, to=10)
spinbox.pack()

root.mainloop()

'''Explanation:

Spinbox(): Creates a numeric input field with increment/decrement arrows.
from_ / to: Defines the allowed range.
pack(): Places the widget in the window.'''