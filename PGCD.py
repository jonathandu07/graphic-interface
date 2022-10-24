# trouver le plus grand diviseur commun et le plus petit multiple commun
import select
from tkinter import*
from math import gcd
from tkinter import ttk
from turtle import width

def action(event):
    select =listCombo.get()
    #récupération de la valeur de m
    m = int(entry_m.get())
    #récupération de la valeur de n
    n = int(entry_n.get())
    
    # pgcd de m et n
    pgcd = gcd(m,n)
    
    # ppcm de m et n
    ppcm = int((m*n)/pgcd)
    
    if (select == 'PGCD'):
        lblResult['text'] = "PGCD =" + str(pgcd)
        
    else:
        lblResult['text'] = "PPCM =" + str(ppcm)    

root =Tk()
root.geometry("350x170")

#création du lable et du champs de saisi pour l'entier m
lbl_m = Label(root, text = "entrer valeur de m")
lbl_m.place(x = 10 , y = 20)
entry_m = Entry(root)
entry_m.place(x = 150 , y = 20)

#création du lable et du champs de saisi pour l'entier n
lbl_n = Label(root, text = "entrer valeur de n")
lbl_n.place(x = 10 , y = 50)
entry_n = Entry(root)
entry_n.place(x = 150 , y = 50)

# création de la liste combo box
listCombo = ttk.Combobox(root, values = ['PGCD', 'PPCM'])
listCombo.place(x = 150, y = 80, width= 120)
listCombo.bind("<<ComboboxSelected>>", action)

#création du label qui affiche le résultat
lblResult = Label(root, text = 'Résultat')
lblResult.place(x = 150, y = 110)
root.mainloop()