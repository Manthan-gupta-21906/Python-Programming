'''The Message widget is used to display multi-line text with automatic word wrapping. It is useful for showing longer messages or descriptions in a formatted way.

message = Message(master, option=value)'''

from tkinter import *

main = Tk()

ourMessage = "This is our Message"
messageVar = Message(main, text=ourMessage)
messageVar.config(bg="lightgreen")
messageVar.pack()

main.mainloop()

'''Explanation:

Message(): Creates a message widget with word wrapping.
text: Specifies the message to display.
config(bg=...): Sets background color.
pack(): Places the widget in the window.'''
