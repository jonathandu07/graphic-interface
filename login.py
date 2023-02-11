from tkinter import *


def Login_Window_open():
    Login_Window = Tk()
    Login_Window.title("Login")
    Login_Window.geometry("470x400")
    Login_Window.minsize(470,400)
    Login_Window.maxsize(470,400)
    Login_Window.config(background="#181818")
    Login_frame = Frame(Login_Window, bg="#707070")
    nom = Label(Login_frame, text="Nom...",font=("Arial",20), bg="#f7f7ff", fg="#181818", width=15, height=1)
    nom.grid(row=0, column=0)
    global NomLogin_entry
    NomLogin_entry = Entry(Login_Frame,font=("Arial",18), bg="#707070", fg="#181818", width=25)
    NomLogin_entry.grid(row=0, column=1)
    
    Login_frame.pack(expand=YES)
    Login_Window.mainloop()
    
Menu_window = Tk()
Menu_window.title("Menu : ")
Menu_window.geometry("350x175")
Menu_window.minsize(350, 175)
Menu_window.maxsize(350, 175)
Menu_window.config(background ="#0a0b0a")

#création d'une frame
Menu_frame = Frame(Menu_window, width=310, height=135, bg ="#091226")
Menu_frame.pack(expand=YES)

#faire afficher les deux bouttons

#Création boutton login
Login_boutton = Button(Menu_frame, text="Login",font=("Arial",20), bg="#f7f7ff", fg="#181818", width=8, height=3, command=Login_Window_open)
Login_boutton.grid(row=0, column=0,)

#Création boutton Inscription
Login_register = Button(Menu_frame, text="Register",font=("Arial",20), bg="#E5E5E5", fg="#181818", width=8, height=3)
Login_register.grid(row=0, column=1,)

Menu_window.mainloop()