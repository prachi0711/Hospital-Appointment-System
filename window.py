import tkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid = " + delete_box_ent.get())

    delete_box_ent.delete(0, END)


    conn.commit()
    conn.close()

def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)

    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.place(x=850, y=200)
    
    conn.commit()
    conn.close()


root = Tk()
root.title("Welcome")
Label(root,text="Appointments",font="Arial 32").pack(pady=50)


root.left = Frame(root, width=700, height=1350, bg='lightblue')
root.left.pack(side = LEFT)

root.right = Frame(root, width=700, height=1350, bg='steelblue')
root.right.pack(side = RIGHT)


def login():
    root.destroy()
    import doctor_login

b2=Button(root, text="Log Out",cursor="hand2", command=login).place(x=330,y=500)

query_btn = Button(root, text="Show Appointment", width=20, height=2,cursor="hand2", command=query)
query_btn.place(x=280, y=210)

delete_btn = Button(root, text="Delete Appointment", width=20, height=2, cursor="hand2", command=delete)
delete_btn.place(x=280, y=350)

delete_box = Label(root, text="Select ID")
delete_box.place(x=200, y=290)

delete_box_ent = Entry(root, width=30 )
delete_box_ent.place(x=280, y=290)


root.geometry("1350x700+0+0")

mainloop()