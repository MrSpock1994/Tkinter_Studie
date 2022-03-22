from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Learn to code")
# root.iconbitmap("INSERT HERE THE IMAGE PATH")
my_img = ImageTk.PhotoImage(Image.open("INSERT HERE THE PATH"))
my_label = Label(image=my_img)
my_label.pack()
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()
root.mainloop()