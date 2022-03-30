from tkinter import *


root = Tk()
root.title("Learning Tkinter")

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()


def slide():
    my_label = Label(root, text=horizontal.get())
    my_label.pack()


my_btn = Button(root, text="Click me", command=slide).pack()
root.mainloop()
