from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Learning Tkinter")
root.filename = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("png files", "*.png"),
                                                                                             ("all files", "*.*")))
mylabel = Label(root, text=root.filename).pack()

root.mainloop()
