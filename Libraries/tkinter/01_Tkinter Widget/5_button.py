'''The Button widget is a clickable component used to perform an action when pressed, such as submitting data or closing a window. Below is the syntax:

button = tk.Button(master, option=value)

Example: This example creates a window titled “Counting Seconds” with a Stop button. When the button is clicked, the application closes.'''

import tkinter as tk

root = tk.Tk()
root.title("Counting Seconds") # will give title to window 

button = tk.Button(root, text="Stop", width=25, command=root.destroy)
button.pack()

root.mainloop()

'''Explanation:

tk.Button(): Creates a button widget.
command=root.destroy: Closes the application when the button is clicked.
button.pack(): Places the button in the window.'''