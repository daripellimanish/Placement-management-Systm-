from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

window=Tk()

submit_var = StringVar()


def submit():
    e = submit_var.get()

    if e == "Student":
        window.destroy()
        os.system('std_login.py')

    elif e == "Company":
        window.destroy()
        os.system('cmp_login.py')

    elif e == "Admin":
        window.destroy()
        os.system('Admin_login.py')

    else:
        messagebox.showerror("","Sorry,You dont have access to the system")


def cancel():
    window.destroy()


icon = PhotoImage(file='logo.gif')
window.iconphoto(True,icon)

labelphoto = Label(window,image=icon)
labelphoto.pack()



lab = Label(window,text='USER TYPE',font='Verdana 10 bold',bg="Cadet blue",fg='white')
lab.place(y=265,x=60)

entry = ttk.Combobox(window,textvariable=submit_var,width=40)
entry['values'] = ("Student","Company","Admin")
entry.place(y=270,x=200)

button_frame = Frame(window,height=100,width=200,padx=20,bg='Cadet Blue')
button_frame.place(x=180,y=300)

submit = Button(button_frame,text='Submit',font='Verdana 10 bold',command=submit)
submit.place(x=10,y=20)

cancel = Button(button_frame,text='Cancel',font='Verdana 10 bold',command=cancel)
cancel.place(x=100,y=20)



window.title("Home Page")

window.geometry("600x500")
window.config(bg="Cadet blue")
window.mainloop()
