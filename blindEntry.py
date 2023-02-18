from tkinter import *
size = "400x320"

window =Tk()
window.title ("vidéo")
window.geometry (size)
window.minsize (400,320)
window.config(background="grey")
Entry_pass = Entry(window, font=("Arial", 20), bg = "white", fg ="black",width=20, show="*")
Entry_pass.pack(expand=YES)

#show permet de cacher la valeur d'un entry
window.mainloop()