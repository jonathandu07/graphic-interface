from tkinter import *
import os
def register():
    nom = NomRegister_entry.get()
    password = passwordRegister_entry.get()
    File_register_name = os.listdir()
    if str(nom) + ".txt" in File_register_name:
        print ("Erreur le nom d'utilistateur existe déjà" + str(nom))
    else :
        Filee = open(nom, "w")
    
def Login_Window_open():
    Login_Window = Tk()
    Login_Window.title("Login")
    Login_Window.geometry("470x400")
    Login_Window.minsize(470, 400)
    Login_Window.maxsize(470, 400)
    Login_Window.config(background="#181818")
    Login_frame = Frame(Login_Window, bg="#707070")
    nom = Label(Login_frame, text="Nom...", font=("Arial", 20),
                bg="#f7f7ff", fg="#181818", width=15, height=1)
    nom.grid(row=0, column=0)
    global NomLogin_entry
    NomLogin_entry = Entry(Login_frame, font=(
        "Arial", 18), bg="#707070", fg="#181818", width=25)
    NomLogin_entry.grid(row=0, column=1)

    # space
    Space = Label(Login_frame, text="", bg="#707070", height=1)
    Space.grid(row=1, column=0)

    # mot de passe
    password = Label(Login_frame, text="Mot de passe...", font=(
        "Arial", 20), bg="#f7f7ff", fg="#181818", width=15, height=1)
    password.grid(row=2, column=0)
    global password_entry
    password_entry = Entry(Login_frame, font=(
        "Arial", 18), bg="#707070", fg="#181818", width=25)
    password_entry.grid(row=2, column=1)

    # space
    Space = Label(Login_frame, text="", bg="#707070", height=1)
    Space.grid(row=4, column=0)

    # Bouton Login
    Login_button = Button(Login_frame, text="Login", font=(
        "Arial", 20), bg="#091226", fg="#f7f7ff", width=8, height=1,)
    Login_button.grid(row=5, column=0,)

    Login_frame.pack(expand=YES)
    Login_Window.mainloop()


def Register_Window_open():
    Register_Window = Tk()
    Register_Window.title("Login")
    Register_Window.geometry("470x400")
    Register_Window.minsize(470, 400)
    Register_Window.maxsize(470, 400)
    Register_Window.config(background="#181818")
    Register_frame = Frame(Register_Window, bg="#707070")
    nom = Label(Register_frame, text="Nom...", font=("Arial", 20),
                bg="#f7f7ff", fg="#181818", width=15, height=1)
    nom.grid(row=0, column=0)
    global NomRegister_entry
    NomRegister_entry = Entry(Register_frame, font=(
        "Arial", 18), bg="#707070", fg="#181818", width=25)
    NomRegister_entry.grid(row=0, column=1)

    # space
    Space = Label(Register_frame, text="", bg="#707070", height=1)
    Space.grid(row=1, column=0)

    # mot de passe
    passwordRegister = Label(Register_frame, text="Mot de passe...", font=(
        "Arial", 20), bg="#f7f7ff", fg="#181818", width=15, height=1)
    passwordRegister.grid(row=2, column=0)
    global passwordRegister_entry
    passwordRegister_entry = Entry(Register_frame, font=(
        "Arial", 18), bg="#707070", fg="#181818", width=25)
    passwordRegister_entry.grid(row=2, column=1)

    # space
    Space = Label(Register_frame, text="", bg="#707070", height=1)
    Space.grid(row=3, column=0)
    
    # Adresse mail
    Mail = Label(Register_frame, text="Adresse mail...", font=(
        "Arial", 20), bg="#f7f7ff", fg="#181818", width=15, height=1)
    Mail.grid(row=4, column=0)
    global Mail_entry
    Mail_entry = Entry(Register_frame, font=(
        "Arial", 18), bg="#707070", fg="#181818", width=25)
    Mail_entry.grid(row=4, column=1)

    # space
    Space = Label(Register_frame, text="", bg="#707070", height=1)
    Space.grid(row=5, column=0)

    # Bouton Register
    Register_button = Button(Register_frame, text="Register", font=(
        "Arial", 20), bg="#091226", fg="#f7f7ff", width=8, height=1,)
    Register_button.grid(row=6, column=0,)

    Register_frame.pack(expand=YES)
    Register_Window.mainloop()


Menu_window = Tk()
Menu_window.title("Menu : ")
Menu_window.geometry("350x175")
Menu_window.minsize(350, 175)
Menu_window.maxsize(350, 175)
Menu_window.config(background="#0a0b0a")

# création d'une frame
Menu_frame = Frame(Menu_window, width=310, height=135, bg="#091226")
Menu_frame.pack(expand=YES)

# faire afficher les deux bouttons

# Création boutton login
Login_boutton = Button(Menu_frame, text="Login", font=(
    "Arial", 20), bg="#f7f7ff", fg="#181818", width=8, height=3, command=Login_Window_open)
Login_boutton.grid(row=0, column=0,)

# Création boutton Inscription
Login_register = Button(Menu_frame, text="Register", font=(
    "Arial", 20), bg="#E5E5E5", fg="#181818", width=8, height=3, command=Register_Window_open)
Login_register.grid(row=0, column=1,)

Menu_window.mainloop()
