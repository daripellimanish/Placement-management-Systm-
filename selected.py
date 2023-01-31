from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

window3 = Tk()

name3_var = StringVar()
reg3_var = StringVar()
com3_var = StringVar()
cgpa3_var = StringVar()
sector3_var = StringVar()
year3_var = StringVar()
search3_var = StringVar()

f31 = Frame(window3)
f31.place(x=330, y=20)

title = Label(f31, text="Selected Students", font=("Time Roman", 45, "bold"), bg="white", padx=10, pady=10,
              relief=RIDGE, bd=10)
title.pack(fill="both")

f32 = Frame(window3, width=350, height=400, bg="#37948e")
f32.place(x=30, y=140)

nameL3 = Label(f32, text='Full name ', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#37948e", fg="white")
nameL3.place(x=10, y=10)

nameE3 = Entry(f32, textvariable=name3_var, width=25)
nameE3.place(x=150, y=14)

regL3 = Label(f32, text='Registration no.', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#37948e", fg="white")
regL3.place(x=10, y=60)

regE3 = Entry(f32, textvariable=reg3_var, width=25)
regE3.place(x=150, y=64)

comL = Label(f32, text='Company Name', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#37948e", fg="white")
comL.place(x=10, y=110)

comE = Entry(f32, textvariable=com3_var, width=25)
comE.place(x=150, y=114)

cgpaL3 = Label(f32, text='CGPA', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#37948e", fg="white")
cgpaL3.place(x=10, y=160)

cgpaE3 = Entry(f32, textvariable=cgpa3_var, width=25)
cgpaE3.place(x=150, y=164)

sectorL = Label(f32, text='Sector', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#37948e", fg="white")
sectorL.place(x=10, y=210)

sectorE = Entry(f32, textvariable=sector3_var, width=25)
sectorE.place(x=150, y=214)

yearL3 = Label(f32, text='Year Of Joining', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#37948e", fg="white")
yearL3.place(x=10, y=250)

yearE3 = Entry(f32, textvariable=year3_var, width=25)
yearE3.place(x=150, y=254)


def DisplayData3():
    mydb = mysql.connector.connect(host='localhost', user='root', password='Mudassir@2003', database='placement')
    cur = mydb.cursor()
    cur.execute("select * from selected")
    result = cur.fetchall()
    if len(result) != 0:
        selected.delete(*selected.get_children())
        for row in result:
            selected.insert('', END, values=row)
    mydb.commit()
    mydb.close()


def submit3():
    for i in selected.get_children():
        selected.delete(i)
    mydb = mysql.connector.connect(host='localhost', user='root', password='Mudassir@2003', database='placement')
    cur = mydb.cursor()
    cur.execute("insert into selected values(%s,%s,%s,%s,%s,%s)",
                (name3_var.get(), reg3_var.get(), com3_var.get(), cgpa3_var.get(), sector3_var.get(), year3_var.get()))
    cur.execute("Select * from selected")
    rows = cur.fetchall()
    for row in rows:
        selected.insert('', END, values=row)

    mydb.commit()
    mydb.close()


def update3():
    mydb = mysql.connector.connect(host='localhost', user='root', password='Mudassir@2003', database='placement')
    cur = mydb.cursor()
    cur.execute(
        "update selected set Full_name = %s,Company_name=%s,CGPA=%s,Sector=%s,Year_of_joining=%s where registration_number =%s ",
        (name3_var.get(), com3_var.get(), cgpa3_var.get(), sector3_var.get(), year3_var.get(), reg3_var.get()))
    cur.execute("Select * from selected")
    rows = cur.fetchall()
    for row in rows:
        selected.insert('', END, values=row)

    messagebox.showinfo("Successful", "Data added successfully!")

    mydb.commit()
    mydb.close()


def cancel3():
    window3.destroy()


def delete3():
    for i in selected.get_children():
        selected.delete(i)
    mydb = mysql.connector.connect(host='localhost', user='root', password='Mudassir@2003', database='placement')
    cur = mydb.cursor()
    sql = 'delete from selected where registration_number="%s"' % reg3_var.get()
    cur.execute(sql)
    mydb.commit()
    messagebox.showinfo("Record deleted", reg3_var.get() + " this record is deleted Succussfullly")
    cur.execute("Select * from selected")
    rows = cur.fetchall()
    for row in rows:
        selected.insert('', END, values=row)

    mydb.close()
    reset3()


def reset3():
    name3_var.set("")
    reg3_var.set("")
    com3_var.set("")
    cgpa3_var.set("")
    sector3_var.set("")
    year3_var.set("")


def search3():
    for i in selected.get_children():
        selected.delete(i)
    mydb = mysql.connector.connect(host='localhost', user='root', password='Mudassir@2003', database='placement')
    cur = mydb.cursor()
    sql = 'select * from selected where registration_number="%s"' % search3_var.get()
    cur.execute(sql)
    result = cur.fetchone()
    name3_var.set(result[0])
    reg3_var.set(result[1])
    com3_var.set(result[2])
    cgpa3_var.set(result[3])
    sector3_var.set(result[4])
    year3_var.set(result[5])

    rows = cur.fetchall()
    for row in rows:
        selected.insert('', END, values=row)
    mydb.close()
    selected.insert('', END, values=result)
    reset3()





frame13 = Frame(window3, width=840, height=450, bg="#37948e")
frame13.place(x=400, y=140)

search_frame3 = Frame(frame13, height=100, width=500, bg="#37948e")
search_frame3.place(x=100, y=20)

search_text = Entry(search_frame3, width=50, textvariable=search3_var)
search_text.place(x=0, y=20)

search_b3 = Button(search_frame3, text='Search',font='Verdana 10 bold', command=search3)
search_b3.place(x=320, y=17)

view_b1 = Button(search_frame3,text='View All', font='Verdana 10 bold', command=DisplayData3)
view_b1.place(x=395, y=17)


submit_b3 = Button(window3, text='Submit',font='Verdana 10 bold', command=submit3)
submit_b3.place(x=30, y=550)

cancel_b3 = Button(window3, text='Cancel', font='Verdana 10 bold', command=cancel3)
cancel_b3.place(x=100, y=550)

update_b3 = Button(window3, text='Update', font='Verdana 10 bold', command=update3)
update_b3.place(x=170, y=550)

delete_b3= Button(window3, text='Delete',font='Verdana 10 bold', command=delete3)
delete_b3.place(x=245, y=550)

reset_b3 = Button(window3, text='Reset',font='Verdana 10 bold', command=reset3)
reset_b3.place(x=310, y=550)

table_frame3 = Frame(frame13, bg='black', width=350, height=450, )
table_frame3.place(x=20, y=100)


scroll_x = Scrollbar(table_frame3, orient=HORIZONTAL)
scroll_y = Scrollbar(table_frame3, orient=VERTICAL)

selected = ttk.Treeview(table_frame3, height=14,
                        columns=("Full name", "Registration no.", "Company Name", "CGPA", "Sector", "Year Of Joining"))
selected.place(x=30, y=150)

selected['show'] = 'headings'

selected.heading('Full name', text='Full name')
selected.heading('Registration no.', text='Regestration no.')
selected.heading('Company Name', text='Company Name')
selected.heading('CGPA', text='CGPA')
selected.heading('Sector', text='Sector')
selected.heading('Year Of Joining', text='Year Of Joining')
selected.pack()

selected['show'] ='headings'

selected.column('Full name', width=150,minwidth=100)
selected.column('Registration no.', width=150,minwidth=100)
selected.column('Company Name', width=100,minwidth=100)
selected.column('CGPA', width=100,minwidth=100)
selected.column('Sector', width=100,minwidth=50)
selected.column('Year Of Joining', width=100,minwidth=70)

vsb = ttk.Scrollbar(window3, orient="vertical", command=selected.yview)
vsb.place(x=1230, y=235, height=200 + 20)

hsb = ttk.Scrollbar(window3, orient="horizontal", command=selected.xview)
hsb.place(x=430, y=535, width=700, height=20 + 0)

selected.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
selected.pack(fill=BOTH, expand=True)

selected.pack()
DisplayData3()

window3.geometry("1250x750")
window3.config(bg="#5f9ea0")
window3.mainloop()
