from tkinter import*

def action1(event):
    root['background'] = 'yellow'
    
def action2(event):
    root['background'] = 'black'
       
root = Tk()
root.geometry("300x200")
root.bind('<Enter>', action1)
root.bind('<Leave>', action2)

root.mainloop()