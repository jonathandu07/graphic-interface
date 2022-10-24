from logging import root
from tkinter import *


def action(event):
    s = int(sp.get())
    root.geometry("{}x{}".format(350 + s*25, 150 + s*25))
    
root = Tk()
root.geometry("350x150")

lblResize = Label(root, text= "reseize window")
lblResize.pack()

sp = Spinbox(root, from_ = 1, to = 30)
sp.pack()
sp.bind('<Button-1>', action)

root.mainloop()