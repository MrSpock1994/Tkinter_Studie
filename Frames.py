from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning Tkinter")
# root.iconbitmap(" IMAGE PATH HERE")

frame = LabelFrame(root, text="This is my Frame", padx=5, pady=5)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't click here")
b.grid(row=0, column=0)

b2 = Button(frame, text="Don't click here")
b2.grid(row=1, column=0)
root.mainloop()

