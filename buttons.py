from tkinter import *

root = Tk()


def myclick():
    mylabel = Label(root, text="Look i Click a Button!")
    mylabel.pack()


myButton = Button(root, text="Click Me!", command=myclick, fg="blue", bg="red")
myButton.pack()

root.mainloop()
