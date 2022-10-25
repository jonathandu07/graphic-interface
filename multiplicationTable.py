from tkinter import *
from tkinter import ttk

def action(event):
    s =listCombo.get()
    N = int(s[-1])
    ResultLabel['text']= "Table de multiplication de " + str(N)
    for i in range (0, 10):
        ResultLabel['text']= ResultLabel['text'] + "\n" + str(i) + " X " + str(N) + " = " + str(i*N)
        
root = Tk()
root.title("table de multiplication")
root.geometry("300x250")

ResultLabel = Label(root, text = 'résulat.....')
ResultLabel.place(x = 50, y = 70)

listNumber = ['table de multiplication de : 1',
              'table de multiplication de : 2',
              'table de multiplication de : 3',
              'table de multiplication de : 4',
              'table de multiplication de : 5',
              'table de multiplication de : 6',
              'table de multiplication de : 7',
              'table de multiplication de : 8',
              'table de multiplication de : 9'
              ]
listCombo = ttk.Combobox(root, values = listNumber, width=25)
listCombo.place(x = 50, y = 10)
listCombo.bind("<<ComboboxSelected>>", action)
root.mainloop()