import tkinter as tk
from tkinter import messagebox

import mysql.connector
from tkinter import *
import os

win = Tk()


def clear():
    userentry.delete(0, END)
    passentry.delete(0, END)


def close():
    win.destroy()


def login():
    if user_name.get() == "" or password.get() == "":
        messagebox.showerror("Error", "Enter User Name And Password", parent=win)
    else:
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="Mudassir@2003", database="placement")
            cur = con.cursor()

            cur.execute("select * from students where student_name=%s and Pass=%s",
                        (user_name.get(), password.get()))
            row = cur.fetchall()

            if row == None:
                messagebox.showerror("Error", "Invalid User Name And Password", parent=win)

            os.system('selected.py')

            close()

            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=win)



win.title("login")

win.maxsize(width=500, height=500)
win.minsize(width=500, height=500)

heading = Label(win, text="Admin Login", font='Verdana 25 bold', bg='cadet blue', fg='white')
heading.place(x=120, y=150)

username = Label(win, text="User Name :", font='Verdana 12 bold', bg="Cadet blue", fg='white')
username.place(x=80, y=220)

userpass = Label(win, text="Password :", font='Verdana 12 bold', bg="Cadet blue", fg='white')
userpass.place(x=80, y=260)

user_name = StringVar()
password = StringVar()

userentry = Entry(win, width=40, textvariable=user_name)
userentry.focus()
userentry.place(x=200, y=223)

passentry = Entry(win, width=40, show="*", textvariable=password)
passentry.place(x=200, y=260)

btn_login = Button(win, text="Login", font='Verdana 10 bold', command=login)
btn_login.place(x=200, y=293)

btn_clr = Button(win, text="Clear", font='Verdana 10 bold', command=clear)
btn_clr.place(x=260, y=293)
#
# btn_ = Button(win, text="SignUp", font='Verdana 10 bold', command=signup)
# btn_login.place(x=320, y=293)

win.config(bg="#5f9ea0")

win.mainloop()
