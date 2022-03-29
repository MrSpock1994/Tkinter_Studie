from tkinter import *


root = Tk()
root.title("Learning Tkinter")


def open_window():
    top = Toplevel()
    label1 = Label(top, text="Hello World")
    label1.pack()
    btn2 = Button(top, text="Close window", command=top.destroy)
    btn2.pack()


btn = Button(root, text="Open second window", command=open_window).pack()

root.mainloop()
