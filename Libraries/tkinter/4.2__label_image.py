import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

# Load JPEG image using PIL

pil_img = Image.open(r"D:\Wallpaper\marvels-spider-man-3840x2160-12891.jpg")
pil_img = pil_img.resize((800, 600))  # width, height
img = ImageTk.PhotoImage(pil_img)

# Create label with image
label = tk.Label(root, image=img)
label.pack()    

# Keep a reference to avoid garbage collection
label.image = img

root.mainloop()