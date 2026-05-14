'''Color Option in Tkinter
Tkinter widgets support various color options that allow you to customize their appearance, including:

Background (bg) and Foreground (fg) colors
Active background (activebackground) and active foreground (activeforeground) colors for buttons
Selection colors for input fields'''

import tkinter as tk

root = tk.Tk()
root.title("Color Options in Tkinter")

# Create a button with active background and foreground colors
button = tk.Button(root, text="Click Me", activebackground="blue", activeforeground="white")
button.pack()

# Create a label with background and foreground colors
label = tk.Label(root, text="Hello, Tkinter!", bg="lightgray", fg="black")
label.pack()

# Create an Entry widget with selection colors
entry = tk.Entry(root, selectbackground="lightblue", selectforeground="black")
entry.pack()

root.mainloop()

'''bg / fg: Sets default background and text color.
activebackground/activeforeground: Colors applied when the button is pressed.
selectbackground/selectforeground: Colors for text selection in Entry or Text widgets.'''