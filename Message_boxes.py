from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title("Learning Tkinter")

# showwarning, showerror, askquestion, askokcancel, askyesno


def popup():
    # messagebox.showinfo("This is my Popup!", "Hello World!")
    resp = messagebox.askyesno("This is my Popup!", "Hello World!")
    Label(root, text=resp)
    if resp == 1:
        Label(root, text="You clicked Yes!").pack()
    else:
        Label(root, text="You clicked No!").pack()


b = Button(root, text="Popup", command=popup)
b.pack()
root.mainloop()
