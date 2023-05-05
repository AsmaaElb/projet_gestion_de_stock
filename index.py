from tkinter import *
from tkinter import messagebox
import sqlite3
import webbrowser
import tkinter as tk
from tkinter import ttk
import tkinter.ttk
from tkinter import Toplevel

import webbrowser
import subprocess

background="#06283D"
framebg="#EDEDED"
framefg="#06283D"

# connexion à la base de données
conn = sqlite3.connect('stock2.db')
c = conn.cursor()
# création de la table users
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT NOT NULL UNIQUE,
              password TEXT NOT NULL)''')
conn.commit()




# fonction pour insérer un nouvel utilisateur dans la base de données
def insert_user(username, password,is_admin=False):
    try:
        # vérifier si l'utilisateur est admin pour ajouter un nouvel utilisateur admin
        if username == "admin" and not is_admin:
            messagebox.showerror("Error", "Only admins can create an admin user")
            return
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "User registered successfully")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists")
# fonction pour vérifier si les informations de connexion sont valides


def login(username, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    if user is not None :
        messagebox.showinfo("Success", "Login successful")
        subprocess.run(["python", "mbox.py", "--logged_in"])
    else:
        messagebox.showerror("Error", "Invalid username or password")

Window=Tk()
Window.title=("Login Systeme")
Window.geometry("1240x630+210+99")
Window.config(bg=background)
Window.resizable(False,False)

#icon image
image_icon=PhotoImage(file="Image/icon.png")
Window.iconphoto(False,image_icon)

#background image
frame=Frame(Window,bg="red")
frame.pack(fill=Y)
backgroundimage=PhotoImage(file="Image/LOGIN.png")
Label(frame,image=backgroundimage).pack()

##############
def connect():
    username = user.get()
    password = code.get()
    
    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter username and password")
    elif username == 'admin' and password == '1234':
        Window.destroy()  # fermer la fenêtre de connexion
        import admin  # importer le fichier admin.py
    else:
        login(username, password)
        


def register():
    username = user.get()
    password = code.get()
    insert_user(username, password)

###############-----------------------------------------------------------------------------------------------
def user_enter(e):
     user.delete(0,'end')
def user_leave(e):
     name=user.get()
     if name=='':
          user.insert(0,'Username')
user=Entry(frame,width=18,fg="#fff",border=0,bg="#375174",font=('Arial Bold',24))
user.insert(0,'UserID')
user.bind("<FocusIn>",user_enter)
user.bind("<FocusOut>",user_leave)
user.place(x=490,y=278)
###############-----------------------------------------------------------------------------------------------
def password_enter(e):
     code.delete(0,'end')
def password_leave(e):
     if code.get()=='':
          code.insert(0,'Password')
code=Entry(frame,width=18,fg="#fff",border=0,bg="#375174",font=('Arial Bold',24))
code.insert(0,'Password')
code.bind("<FocusIn>",password_enter)
code.bind("<FocusOut>",password_leave)
code.place(x=490,y=370)
####Hide and show button

button_mode=True
def hide():
     global button_mode
     if button_mode:
          eyeButton.config(image=closeeye,activebackground="white")
          code.config(show="*")
          button_mode=False
     else:
          eyeButton.config(image=openeye,activebackground="white")
          code.config(show="")
          button_mode=True
     

openeye=PhotoImage(file="Image/openeye.png")
closeeye=PhotoImage(file="Image/close eye.png")
eyeButton=Button(frame,image=openeye,bg="#375174",bd=0,command=hide)
eyeButton.place(x=780,y=375)
###############-----------------------------------------------------------------------------------------------

loginButton=Button(Window,text="LOGIN",bg="#1f5675",width=10,height=1,fg="white",font=("arial",16,'bold'),bd=0,command=connect)

loginButton.place(x=550,y=570)

label=Label(Window,text="Don't have an account?",fg="#fff",bg="#00264d",font=('Microsot YaHei UI Light',9))
label.place(x=500,y=500)

registerButton=Button(Window,width=10,text="add new user",borde=0,bg="#00264d",cursor='hand2',fg="#57a1f8",command=register)
registerButton.place(x=650,y=500)

Window.mainloop()
