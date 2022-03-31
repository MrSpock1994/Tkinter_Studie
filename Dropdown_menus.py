from tkinter import *


root = Tk()
root.title("Learning Tkinter")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
selected = StringVar()
selected.set(days[0])

drop = OptionMenu(root, selected, *days)
drop.pack()


def show():
    my_label = Label(root, text=selected.get())
    my_label.pack()


my_button = Button(root, text="Show Selection", command=show)
my_button.pack()
root.mainloop()
