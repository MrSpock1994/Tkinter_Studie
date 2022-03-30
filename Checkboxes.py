from tkinter import *


root = Tk()
root.title("Learning Tkinter")


def show():
    my_label = Label(root, text=var.get())
    my_label.pack()


var = StringVar()

c = Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

my_btn = Button(root, text="Show selection", command=show)
my_btn.pack()
root.mainloop()
