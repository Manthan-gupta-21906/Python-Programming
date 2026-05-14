'''Combobox
The Combobox widget (from tkinter.ttk) provides a drop-down list that allows users to select one value from a predefined set of options. Below is the syntax:

combo = ttk.Combobox(master, values=[...], state='readonly')'''

import tkinter as tk
from tkinter import ttk

def select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)

root = tk.Tk()
root.title("Combobox Example")

label = tk.Label(root, text="Selected Item:")
label.pack(pady=10)

# Create a Combobox widget
combo_box = ttk.Combobox(
    root,
    values=["Option 1", "Option 2", "Option 3"],
    state="readonly"
)
combo_box.pack(pady=5)

combo_box.set("Option 1")

combo_box.bind("<<ComboboxSelected>>", select)
root.mainloop()

