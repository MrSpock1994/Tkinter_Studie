from tkinter import *

root = Tk()

e = Entry(root)
e.pack()
e.get()
e.insert(0, "Enter your name")


def myclick():
    mylabel = Label(root, text=f"Hello {e.get()}, name validated")
    mylabel.pack()


myButton = Button(root, text="Click to validate your name!", command=myclick, fg="blue", bg="red")
myButton.pack()

root.mainloop()
