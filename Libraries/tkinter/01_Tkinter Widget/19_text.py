'''Text
The Text widget is used to display or edit multi-line text. Unlike Entry, it supports multiple lines and text formatting. Below is the syntax:

text = Text(master, option=value)'''

from tkinter import *

root = Tk()
root.title("Text Widget Example")

text_widget = Text(root, height=2, width=30)
text_widget.pack()

text_widget.insert(END, "GeeksforGeeks\nBEST WEBSITE\n")
root.mainloop()

'''Explanation:

Text(): Creates a multi-line text widget.
insert(): Inserts text at a specified position.
END: Appends text at the end'''