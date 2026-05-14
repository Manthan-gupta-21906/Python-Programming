'''Key and Mouse Events
Key events are triggered when a user presses a key on the keyboard. Mouse events are triggered by mouse actions, such as clicking or moving the mouse.'''

import tkinter as tk

def on_key_press(event):
    print(f"Key pressed: {event.keysym}")

def on_left_click(event):
    print(f"Left click at ({event.x}, {event.y})")

def on_right_click(event):
    print(f"Right click at ({event.x}, {event.y})")

def on_mouse_motion(event):
    print(f"Mouse moved to ({event.x}, {event.y})")

root = tk.Tk()
root.title("Advanced Event Handling Example")

root.bind("<KeyPress>", on_key_press)
root.bind("<Button-1>", on_left_click)
root.bind("<Button-3>", on_right_click)
root.bind("<Motion>", on_mouse_motion)

root.mainloop()

'''Explanation:

The on_mouse_motion function is called whenever the mouse moves in the window.
Multiple event types can be handled at the same time.
Event Object
The event object is passed to the callback function when an event occurs. It contains useful information about the event, such as:

event.keysym: The key symbol (e.g., 'a', 'Enter').
event.x and event.y: The x and y coordinates of the mouse event.
event.widget: The widget that triggered the event.'''