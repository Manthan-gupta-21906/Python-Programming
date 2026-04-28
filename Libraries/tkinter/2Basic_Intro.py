import tkinter as tk
#In Tkinter, the Tk() class is used to create the main application window. Every Tkinter program starts by creating exactly one Tk() object. Below is the syntax:

root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
'''Parameter:

screenName (optional): Specifies the display (mainly used on Unix systems with multiple screens).
baseName (optional): Sets the base name for the application (default is the script name).
className (optional): Defines the name of the window class (used for styling and window manager settings).
useTk (optional): A boolean that tells whether to initialize the Tk subsystem (usually left as default 1).'''