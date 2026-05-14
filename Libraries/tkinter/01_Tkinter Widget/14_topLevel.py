'''The Toplevel widget is used to create a separate window in a Tkinter application. It is managed directly by the window manager and is commonly used for dialogs, pop-ups, or secondary windows. Below is the syntax:

top = Toplevel(master, option=value)'''

from tkinter import *
root = Tk()
root.title('GfG')
top = Toplevel()
top.title('Python')
top.mainloop()

'''Explanation:

Toplevel(): Creates a new independent window.
title(): Sets the window title.'''
