from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import os


window = Tk()


name_var = StringVar()
reg_var = StringVar()
pwd_var = StringVar()


f1 = Frame(window)
f1.place(x=180,y=20)

title = Label(f1,text="Company Sign Up",font=("Time Roman",35,"bold"),bg="white",padx=10,pady=10,relief=RIDGE,bd=10)
title.pack(fill="both")

f2 = Frame(window,width=350,height=200,bg="#37948e")
f2.place(x=220,y=140)

nameL = Label(f2,text='Company name ',padx=5,pady=5,font=('Arial',12,"bold"),bg="#37948e",fg="white")
nameL.place(x=10,y=10)

nameE = Entry(f2,textvariable=name_var,width=25)
nameE.place(x=150,y=14)

regL = Label(f2,text='Company Id',padx=5,pady=5,font=('Arial',12,"bold"),bg="#37948e",fg="white")
regL.place(x=10,y=60)

regE = Entry(f2,textvariable=reg_var,width=25)
regE.place(x=150,y=64)

pwdL = Label(f2,text='Password',padx=5,pady=5,font=('Arial',12,"bold"),bg="#37948e",fg="white")
pwdL.place(x=10,y=110)

pwdE = Entry(f2,textvariable=pwd_var,show="*",width=25)
pwdE.place(x=150,y=114)


def cancel():
    window.destroy()
    os.system('common.py')


def reset():
    name_var.set("")
    reg_var.set("")
    pwd_var.set("")

def submit():
    mydb = mysql.connector.connect(host='localhost', user='root', password='Mudassir@2003', database='placement')
    cur = mydb.cursor()
    cur.execute("insert into company values(%s,%s,%s)",
                (name_var.get(), reg_var.get(), pwd_var.get()))
    cur.execute("Select * from students")
    rows = cur.fetchall()
    messagebox.showinfo("", "Registered successfully")

    mydb.commit()
    mydb.close()
    os.system('cmp_login.py')
    reset()

button_frame = Frame(window, bg='cadet blue', height=100, width=400, padx=20)
button_frame.place(x=250, y=350)

sub_b1 = Button(button_frame,text='Submit',font='Verdana 10 bold',command=submit)
sub_b1.place(x=10,y=10)

can_b1 = Button(button_frame,text='Cancel',font='Verdana 10 bold',command=cancel)
can_b1.place(x=90,y=10)

reset_b1 = Button(button_frame,text='Reset',font='Verdana 10 bold',command=reset)
reset_b1.place(x=170,y=10)


window.geometry("800x450")
window.config(bg="#5f9ea0")
window.mainloop()
