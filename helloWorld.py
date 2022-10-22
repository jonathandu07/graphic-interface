from tkinter import * 

def action():
    lbl['text'] = "hello world"

root = Tk()
root.geometry("400x250")
lbl = Label(root, text="..............")
btn = Button(root, text ="cliquez ici", command = action)
btn.place(x = 150, y =50)
lbl.place(x=150, y=100)
root.mainloop()