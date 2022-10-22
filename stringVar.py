from tkinter import * 

def action():
    var.set("hello world............ !")

root = Tk()
root.geometry("400x250")

var = StringVar()
lbl = Label(root, textvariable= var)
btn = Button(root, text ="cliquez ici", command = action)
btn.place(x = 150, y =50)
lbl.place(x=150, y=100)
root.mainloop()