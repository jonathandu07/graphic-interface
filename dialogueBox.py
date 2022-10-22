from tkinter import * 

def action(event):
    #obtenir la valeur du premier champs de saisi
    N = int(entryNumber1.get())
    N2 = 2*N
    #vider le chaps de saisi entryNumber2
    entryNumber2.delete(0, END)
    #insertion de N2 sur le deuxième champs de saisi
    entryNumber2.insert(0, N2)


root = Tk()
root.geometry("400x250")

#création du label et du premier champs de saisi
lblNumber1 = Label(root, text= "entrer la valeur de N")
lblNumber1.place(x = 50, y = 20)

entryNumber1 = Entry(root)
entryNumber1.place(x = 200, y = 20)
entryNumber1.bind('<Return>', action)

#création du label et du deuxième champs de saisi
lblNumber2 = Label(root, text= "Le double de N :")
lblNumber2.place(x = 50, y = 50)

entryNumber2 = Entry(root)
entryNumber2.place(x = 200, y = 50)
root.mainloop()