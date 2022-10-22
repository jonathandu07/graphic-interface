from tkinter import * 

def fermer():
    root.quit()

root = Tk()
root.geometry("400x250")
btn_close = Button(root, text = "fermer fenête", command= fermer)
btn_close.place(x= 150, y = 100)
root.mainloop()