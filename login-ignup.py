from tkinter import *

global root;
root = Tk()

root.geometry('500x350')
root.title("Login Form")


nameVar=StringVar()
emailVar=StringVar()
passVar=StringVar()
genderVar = IntVar()
javaVar= IntVar()
pythonVar= IntVar()
    

#method to add user register data in database    
def addNew():
    name=nameVar.get()
    email=emailVar.get()
    password=passVar.get()
    gender=genderVar.get()
    prog=javaVar.get()
    conn = sqlite3.connect('StudentDatabase.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS StudentTable (Name TEXT,Email TEXT,Password Text,Gender TEXT,Programming TEXT)')
    count=cursor.execute('INSERT INTO StudentTable (Name,Email,Password,Gender,Programming) VALUES(?,?,?,?,?)',(name,email,password,gender,prog))
    
    if(cursor.rowcount>0):
        print ("Signup Done")
    else:
        print ("Signup Error")
    conn.commit()
    

#method to perform login    
def loginNow():
    email=emailVar.get()
    password=passVar.get()
    
    conn = sqlite3.connect('StudentDatabase.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS StudentTable (Name TEXT,Email TEXT,Password Text,Gender TEXT,Programming TEXT)')
    cursor.execute('Select * from StudentTable Where Email=? AND Password=?',(email,password))
    
    if cursor.fetchone() is not None:
        print ("Welcome")
    else:
        print ("Login failed")
    
    conn.commit()
   

 #method to design register window
def registerWindow(): 
    
    registerScreen=Toplevel(root)
    
    registerScreen.title("Registration Here")
    
    registerScreen.geometry('500x500')
    
    label = Label(registerScreen, text="Registration Here",width=20,fg="blue",font=("bold", 20))
    label.place(x=90,y=53)


    nameLabel = Label(registerScreen, text="FullName",width=20,font=("bold", 10))
    nameLabel.place(x=80,y=130)

    nameEntery = Entry(registerScreen,textvar=nameVar)
    nameEntery.place(x=240,y=130)

    emailLabel = Label(registerScreen, text="Email",width=20,font=("bold", 10))
    emailLabel.place(x=68,y=180)

    emailEntry = Entry(registerScreen,textvar=emailVar)
    emailEntry.place(x=240,y=180)

    passLabel = Label(registerScreen, text="Password",width=20,font=("bold", 10))
    passLabel.place(x=78,y=230)

    passEntry = Entry(registerScreen,textvar=passVar,show='*')
    passEntry.place(x=240,y=230)

    genderLabel = Label(registerScreen, text="Gender",width=20,font=("bold", 10))
    genderLabel.place(x=70,y=280)

    Radiobutton(registerScreen, text="Male",padx = 5, variable=genderVar, value=1).place(x=235,y=280)
    Radiobutton(registerScreen, text="Female",padx = 20, variable=genderVar, value=2).place(x=290,y=280)

    labelLanguage = Label(registerScreen, text="Programming",width=20,font=("bold", 10))
    labelLanguage.place(x=88,y=325)

    Checkbutton(registerScreen, text="java", variable=javaVar).place(x=238,y=325)

    Checkbutton(registerScreen, text="python", variable=pythonVar).place(x=310,y=325)

    Button(registerScreen, text='Submit',width=20,bg='blue',fg='white',pady=5,command=addNew).place(x=180,y=380)

    
    
label = Label(root, text="Login Here",width=20,fg="blue",font=("bold", 20))
label.place(x=90,y=53)


emailLabel = Label(root, text="Email",width=20,font=("bold", 10))
emailLabel.place(x=68,y=130)

emailEntry = Entry(root,textvar=emailVar)
emailEntry.place(x=240,y=130)

passwordLabel = Label(root, text="Password",width=20,font=("bold", 10))
passwordLabel.place(x=68,y=180)

passwordEntry = Entry(root,textvar=passVar,show='*')
passwordEntry.place(x=240,y=180)

Button(root, text='Login Now',width=20,bg='blue',fg='white',pady=5,command=loginNow).place(x=180,y=230)

Button(root,text="Have no Accout! Create one",bg="red",fg="white",font=("bold",10),command=registerWindow).place(x=170,y=280)

root.mainloop()