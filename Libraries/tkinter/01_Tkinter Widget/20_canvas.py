'''Canvas
The Canvas widget is used to draw graphics, such as lines, shapes, text, and images. Below is the syntax:

canvas = Canvas(master, option=value)'''

from tkinter import *

root = Tk()
root.title("Canvas Example")

canvas = Canvas(root, width=200, height=60)
canvas.pack()

y = 30
canvas.create_line(0, y, 200, y)
root.mainloop()

'''Explanation:

Canvas(): Creates a drawing area.
create_line(): Draws a line using start and end coordinates.
Canvas supports shapes, images, and custom graphics.'''