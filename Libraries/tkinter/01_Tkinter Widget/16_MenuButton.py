'''MenuButton
The Menubutton widget is used to create a button with a dropdown menu. When clicked, it displays a menu containing different options such as commands or checkbuttons. Below is the syntax:

menubutton = Menubutton(master, option=value)'''

from tkinter import *
top = Tk() 
mb = Menubutton ( top, text = "GfG") 
mb.grid() 
mb.menu = Menu ( mb, tearoff = 0 ) 
mb["menu"] = mb.menu 
cVar = IntVar() 
aVar = IntVar() 
mb.menu.add_checkbutton ( label ='Contact', variable = cVar ) 
mb.menu.add_checkbutton ( label = 'About', variable = aVar ) 
mb.pack() 
top.mainloop()

'''Explanation:

Menubutton(): Creates a button with an attached menu.
Menu(): Defines the dropdown menu.
add_checkbutton(): Adds toggleable options to the menu.
IntVar(): Stores the checked/unchecked state.'''