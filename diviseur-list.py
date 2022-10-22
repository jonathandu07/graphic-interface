# -*- coding: utf-8 -*-
from tkinter import *

def action():
    N = int(entryNombre.get())
    lblDiviseurs['text'] = "Diviseurs de N :"
    for i in range(1, N + 1):
        if(N%i == 0):
            lblDiviseurs['text'] = lblDiviseurs['text']+ " " + str(i) + " "
            
fen = Tk()
fen.geometry("400x175")
lblNombre = Label(fen, text = "entrer la valeur de N")
lblNombre.place(x= 10, y= 20)
entryNombre = Entry(fen)
entryNombre.place(x = 200, y=20)
lblDiviseurs = Label(fen, text = "les diviseurs de N  :")
lblDiviseurs.place(x= 10, y=50)

Valider = Button(fen, text = "Valider", command=action)
Valider.place(x=200, y=90)
fen.mainloop()
