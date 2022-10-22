from tkinter import * 

def action():
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

#création du boutton valider

btn_validate = Button(root, text = 'valider', command=action)
btn_validate.place(x=100, y=150, width=100)

root.mainloop()