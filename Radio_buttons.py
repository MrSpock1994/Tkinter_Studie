from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning Tkinter")
# root.iconbitmap(" IMAGE PATH HERE")

r = IntVar()
r.set(2)
r.get()


def clicked(value):
    mylabel = Label(root, text=value)
    mylabel.pack()


Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()


root.mainloop()
