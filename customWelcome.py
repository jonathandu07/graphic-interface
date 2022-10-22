from argparse import Action
from tkinter import * 

def action(event):
    name = entryName.get()
    var.set("hello" + " " + name )

root = Tk()
root.geometry("400x250")
root.title('message')

#création du label
var = StringVar()
lblResult = Label(root, textvariable= var)
lblResult.place(x=100, y=50)

#création  du champs de saisi

entryName = Entry(root)
entryName.place(x = 100 , y = 100 , width = 150)
entryName.bind('<Return>', action)

root.mainloop()