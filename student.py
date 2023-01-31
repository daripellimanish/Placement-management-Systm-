from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview

import mysql.connector
from tkinter import messagebox
import os

window = Tk()

name_var = StringVar()
reg_var = StringVar()
bran_var = StringVar()
cgpa_var = StringVar()
year_var = StringVar()
phone_var = StringVar()
gender_var = StringVar()
email_var = StringVar()
search_var = StringVar()
del_var = StringVar()
hsc_var = StringVar()
ssc_var = StringVar()
cp_var = StringVar()

f1 = Frame(window)
f1.place(x=330, y=20)

title = Label(f1, text="Student Registration", font=("Time Roman", 40, "bold"), bg="white", padx=10, pady=10,
              relief=RIDGE, bd=10)
title.pack(fill="both")

f2 = Frame(window, width=350, height=550, bg="#37948e")
f2.place(x=30, y=140)

nameL = Label(f2, text='Full name ', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#37948e", fg="white")
nameL.place(x=10, y=10)

nameE = Entry(f2, textvariable=name_var, width=25)
nameE.place(x=150, y=14)

emailL = Label(f2, text='Email id', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#37948e", fg="white")
emailL.place(x=10, y=60)

emailE = Entry(f2, textvariable=email_var, width=25)
emailE.place(x=150, y=64)

phoneL = Label(f2, text='Phone no.', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#37948e", fg="white")
phoneL.place(x=10, y=110)

phoneE = Entry(f2, textvariable=phone_var, width=25)
phoneE.place(x=150, y=114)

genderL = Label(f2, text='Gender', font=('Arial', 12, "bold"), bg="#37948e", fg="white")
genderL.place(x=10, y=160)

genderE = ttk.Combobox(f2, textvariable=gender_var, width=22)
genderE['values'] = ("Female", "Male", "Other")
genderE.place(x=150, y=164)

regL = Label(f2, text='Registration no.', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#37948e", fg="white")
regL.place(x=10, y=210)

regE = Entry(f2, textvariable=reg_var, width=25)
regE.place(x=150, y=214)

branchL = Label(f2, text='Branch', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#37948e", fg="white")
branchL.place(x=10, y=260)

branchE = Entry(f2, textvariable=bran_var, width=25)
branchE.place(x=150, y=264)

yearL = Label(f2, text='Year', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#37948e", fg="white")
yearL.place(x=10, y=310)

yearE = ttk.Combobox(f2, textvariable=year_var, width=22)
yearE['values'] = ("TE", "BE", "MCA")
yearE.place(x=150, y=314)

cgpaL = Label(f2, text='CGPA', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#37948e", fg="white")
cgpaL.place(x=10, y=360)

cgpaE = Entry(f2, textvariable=cgpa_var, width=25)
cgpaE.place(x=150, y=364)

hscL = Label(f2, text='HSC', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#37948e", fg="white")
hscL.place(x=10, y=410)

hscE = Entry(f2, textvariable=hsc_var, width=25)
hscE.place(x=150, y=414)

sscL = Label(f2, text='SSC', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#37948e", fg="white")
sscL.place(x=10, y=460)

sscE = Entry(f2, textvariable=ssc_var, width=25)
sscE.place(x=150, y=464)

cpL = Label(f2, text='CP Profile', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#37948e", fg="white")
cpL.place(x=10, y=510)

cpE = Entry(f2, textvariable=cp_var, width=25)
cpE.place(x=150, y=514)


def next():
    window.destroy()
    os.system('cmp_login.py')


def DisplayData():
    for i in student_table.get_children():
        student_table.delete(i)
    mydb = mysql.connector.connect(host='localhost', user='root', password='Mudassir@2003', database='placement')
    cur = mydb.cursor()
    cur.execute("select * from student_table")
    result = cur.fetchall()
    if len(result) != 0:
        student_table.delete(*student_table.get_children())
        for row in result:
            student_table.insert('', END, values=row)
    mydb.commit()
    mydb.close()


def submit():
    for i in student_table.get_children():
        student_table.delete(i)
    mydb = mysql.connector.connect(host='localhost', user='root', password='Mudassir@2003', database='placement')
    cur = mydb.cursor()
    cur.execute("insert into student_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (name_var.get(), email_var.get(), phone_var.get(), gender_var.get(), reg_var.get(), bran_var.get(),
                 year_var.get(), cgpa_var.get(), hsc_var.get(), ssc_var.get(),cp_var.get()))
    cur.execute("Select * from student_table")
    rows = cur.fetchall()
    for row in rows:
        student_table.insert('', END, values=row)

    messagebox.showinfo("", "Data Added successfully")

    mydb.commit()

    mydb.close()


def update():
    for i in student_table.get_children():
        student_table.delete(i)
    mydb = mysql.connector.connect(host='localhost', user='root', password='Mudassir@2003', database='placement')
    cur = mydb.cursor()
    cur.execute(
        "update student_table set Full_name = %s,Email_Id=%s,Phone_no=%s,Gender=%s,Branch=%s,Year=%s,CGPA=%s,HSC=%s,SSC=%s,CP_Profile=%s where Registration_no =%s ",
        (name_var.get(), email_var.get(), phone_var.get(), gender_var.get(), bran_var.get(), year_var.get(),
         cgpa_var.get(), hsc_var.get(), ssc_var.get(),cp_var.get(), reg_var.get()))
    cur.execute("Select * from student_table")
    rows = cur.fetchall()
    for row in rows:
        student_table.insert('', END, values=row)

    messagebox.showinfo("Successful", "Data updated successfully!")

    mydb.commit()
    mydb.close()


def cancel():
    window.destroy()
    os.system('common.py')


def search():
    for i in student_table.get_children():
        student_table.delete(i)
    mydb = mysql.connector.connect(host='localhost', user='root', password='Mudassir@2003', database='placement')
    cur = mydb.cursor()
    sql = 'select * from student_table where registration_number="%s"' % search_var.get()
    cur.execute(sql)
    result = cur.fetchone()
    name_var.set(result[0])
    email_var.set(result[1])
    phone_var.set(result[2])
    gender_var.set(result[3])
    reg_var.set(result[4])
    bran_var.set(result[5])
    year_var.set(result[6])
    cgpa_var.set(result[7])
    hsc_var.set(result[8])
    ssc_var.set(result[9])
    cp_var.set(result[10])

    rows = cur.fetchall()
    for row in rows:
        student_table.insert('', END, values=row)
    mydb.close()
    student_table.insert('', END, values=result)


def delete():
    for i in student_table.get_children():
        student_table.delete(i)
    mydb = mysql.connector.connect(host='localhost', user='root', password='Mudassir@2003', database='placement')
    cur = mydb.cursor()
    sql = 'delete from student_table where  registration_number="%s"' % reg_var.get()
    cur.execute(sql)
    mydb.commit()
    messagebox.showinfo("Record deleted", reg_var.get() + " this record is deleted Succussfullly")
    cur.execute("Select * from student_table")
    rows = cur.fetchall()
    for row in rows:
        student_table.insert('', END, values=row)
    reset()
    mydb.close()


def reset():
    name_var.set("")
    email_var.set("")
    phone_var.set("")
    gender_var.set("")
    reg_var.set("")
    bran_var.set("")
    year_var.set("")
    cgpa_var.set("")
    hsc_var.set("")
    ssc_var.set("")
    cp_var.set("")


sub_b1 = Button(text='Submit', font='Verdana 10 bold', command=submit)
sub_b1.place(x=30, y=700)

upd_b1 = Button(text='Update', font='Verdana 10 bold', command=update)
upd_b1.place(x=105, y=700)

dlt_b1 = Button(text='Delete',font='Verdana 10 bold', command=delete)
dlt_b1.place(x=180, y=700)

reset_b1 = Button(text='Reset', font='Verdana 10 bold', command=reset)
reset_b1.place(x=250, y=700)

home_b1 = Button(text='Home',font='Verdana 10 bold', command=cancel)
home_b1.place(x=315, y=700)

frame11 = Frame(window, width=840, height=450, bg="#37948e")
frame11.place(x=400, y=140)

next_b1 = Button(text='NEXT >>', font='Verdana 10 bold', command=next)
next_b1.place(x=1100, y=700)



search_frame = Frame(frame11, height=100, width=500, bg="#37948e")
search_frame.place(x=100, y=20)

search_text = Entry(search_frame, width=50, textvariable=search_var)
search_text.place(x=0, y=20)

search_b1 = Button(search_frame, text='Search',font='Verdana 10 bold', command=search)
search_b1.place(x=320, y=17)

view_b1 = Button(search_frame,text='View All', font='Verdana 10 bold', command=DisplayData)
view_b1.place(x=395, y=17)

table_frame = Frame(frame11, width=750, height=900, bg='black')
table_frame.place(x=20, y=100)

scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
scroll_y = Scrollbar(table_frame, orient=VERTICAL)

student_table = ttk.Treeview(table_frame,
                             columns=(
                                 "Full name", "Email Id", "Phone no.", "Gender", "Registration no.", "Branch", "Year",
                                 "CGPA", "HSC", "SSC", "CP Profile"))
student_table.place(x=30, y=150)
student_table['show'] = 'headings'

student_table.heading('Full name', text='Full name')
student_table.heading('Email Id', text='Email Id')
student_table.heading('Phone no.', text='Phone no.')
student_table.heading('Gender', text='Gender')
student_table.heading('Registration no.', text='Registration no.')
student_table.heading('Branch', text='Branch')
student_table.heading('Year', text='Year')
student_table.heading('CGPA', text='CGPA')
student_table.heading('HSC', text='HSC')
student_table.heading('SSC', text='SSC')
student_table.heading('CP Profile', text='CP Profile')

student_table.pack()
student_table['show'] = 'headings'

student_table.column('Full name', width=70, minwidth=70)
student_table.column('Email Id', width=70, minwidth=70)
student_table.column('Phone no.', width=70, minwidth=70)
student_table.column('Gender', width=70, minwidth=70)
student_table.column('Registration no.', width=70, minwidth=70)
student_table.column('Branch', width=70, minwidth=70)
student_table.column('CGPA', width=70, minwidth=70)
student_table.column('Year', width=70, minwidth=70)
student_table.column('HSC', width=70, minwidth=70)
student_table.column('SSC', width=70, minwidth=70)
student_table.column('CP Profile', width=70, minwidth=70)

vsb = ttk.Scrollbar(window, orient="vertical", command=student_table.yview)
vsb.place(x=1230, y=235, height=200 + 20)

hsb = ttk.Scrollbar(window, orient="horizontal", command=student_table.xview)
hsb.place(x=430, y=535, width=700, height=20 + 0)

student_table.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)

student_table.pack(fill=BOTH, expand=1)

DisplayData()

window.geometry("1250x750")
window.config(bg="#5f9ea0")
window.mainloop()
