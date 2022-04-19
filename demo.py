import sqlite3
import tkinter
from tkinter import *
from tkinter import ttk,messagebox
from webbrowser import get

root = Tk()
root.title("Add new appointment")
root.geometry("1350x700+0+0")
root.config(bg="white")

def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid = " + delete_box_ent.get())

    delete_box_ent.delete(0, END)


    conn.commit()
    conn.close()


def submit():
    if name_ent.get()=="" or gender.get()=="select" or time_ent.get()=="":
        messagebox.showerror("error","all feilds are required",parent=root)
    else:
         
        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()


        c.execute("INSERT INTO addresses VALUES (:name_ent, :age_ent, :gender, :location_ent, :time_ent, :phone_ent)",
                {
                    'name_ent': name_ent.get(),
                    'age_ent': age_ent.get(),
                    'gender': gender.get(),
                    'location_ent': location_ent.get(),
                    'time_ent': time_ent.get(),
                    'phone_ent': phone_ent.get()


                } )


        conn.commit()
        conn.close()

        name_ent.delete(0, END)
        age_ent.delete(0, END)
        gender.delete(0, END)
        location_ent.delete(0, END)
        time_ent.delete(0, END)
        phone_ent.delete(0, END)

def update():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    record_id = delete_box_ent.get()


    c.execute("""UPDATE addresses SET
         name = :name,
         age = :age,
         location = :location,
         time = :time,
         phone = :phone

         WHERE oid = :oid""",
         {
             'name' : name_ent_editor.get(),
             'age' : age_ent_editor.get(),
             'location' : location_ent_editor.get(),
             'time' : time_ent_editor.get(),
             'phone' : phone_ent_editor.get(),

             'oid': record_id
             


         })

    conn.commit()
    conn.close()



def edit():
    editor = Tk()
    editor.title("Update A Record")
    editor.geometry("1350x700")

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    
    record_id = delete_box_ent.get()

    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()
    
    print_records = ''
    for record in records[0]:
        print_records += str(record) + "\n"

    name_editor = Label(editor, text="Patient's Name", font=('arial 12'))
    name_editor.place(x=65, y=100) 

    age_editor = Label(editor, text="Age", font=('arial 12'))
    age_editor.place(x=65, y=140)

    question_editor=Label(editor,text="Gender", font=("arial",12)).place(x=60,y=180)
    gender_editor = ttk.Combobox(editor, font=("arial",12),state='readonly',justify=CENTER)
    gender_editor['values']=("select","male","female","others")
    gender_editor.config(width=10, cursor="hand2")
    gender_editor.place(x=275, y=180)
    gender_editor.current(0)

    location_editor = Label(editor, text="Location", font=('arial 12'))
    location_editor.place(x=65, y=220)

    time_editor = Label(editor, text="Appointment Time (HH:MM)", font=('arial 12'))
    time_editor.place(x=65, y=260)

    phone_editor = Label(editor, text="Phone Number", font=('arial 12'))
    phone_editor.place(x=65, y=300)

    save_btn = Button(editor, text="Save", width=20, height=2, cursor="hand2",command=update)
    save_btn.place(x=150, y=400)

    global name_ent_editor
    global age_ent_editor
    global location_ent_editor
    global time_ent_editor
    global phone_ent_editor


    name_ent_editor = Entry(editor, width=30)
    name_ent_editor.place(x=275, y=100)

    age_ent_editor = Entry(editor, width=30)
    age_ent_editor.place(x=275, y=140)

    location_ent_editor = Entry(editor, width=30)
    location_ent_editor.place(x=275, y=220)

    time_ent_editor = Entry(editor, width=30)
    time_ent_editor.place(x=275, y=260)

    phone_ent_editor = Entry(editor, width=30)
    phone_ent_editor.place(x=275, y=300)

    for record in records:
        name_ent_editor.insert(0, record[0])
        age_ent_editor.insert(0, record[1])
        gender_editor.insert(0, record[2])
        location_ent_editor.insert(0, record[3])
        time_ent_editor.insert(0, record[4])
        phone_ent_editor.insert(0, record[5])
        




def logout():
    root.destroy()
    import login3



root.left = Frame(root, width=700, height=720, bg='lightblue')
root.left.pack(side = LEFT)

root.right = Frame(root, width=700, height=720, bg='steelblue')
root.right.pack(side = RIGHT)


root.heading = Label(root.left, text="Enter details", font=('arial 18'), fg='black', bg='lightblue')
root.heading.place(x=220, y=50)


name = Label(root.left, text="Patient's Name", font=('arial 12'), fg='black', bg='lightblue')
name.place(x=65, y=100)

age = Label(root.left, text="Age", font=('arial 12'), fg='black', bg='lightblue')
age.place(x=65, y=140)

question=Label(root.left,text="Gender", font=("arial",12), bg="lightblue",fg="black").place(x=60,y=180)
gender = ttk.Combobox(root.left, font=("arial",12),state='readonly',justify=CENTER)
gender['values']=("select","male","female","others")
gender.config(width=10, cursor="hand2")
gender.place(x=275, y=180)
gender.current(0)

location = Label(root.left, text="Location", font=('arial 12'), fg='black', bg='lightblue')
location.place(x=65, y=220)

time = Label(root.left, text="Appointment Time (HH:MM)", font=('arial 12'), fg='black', bg='lightblue')
time.place(x=65, y=260)

phone = Label(root.left, text="Phone Number", font=('arial 12'), fg='black', bg='lightblue')
phone.place(x=65, y=300)

delete_box = Label(root.left, text="Select ID")
delete_box.place(x=80, y=430)


name_ent = Entry(root.left, width=30)
name_ent.place(x=275, y=100)

age_ent = Entry(root.left, width=30)
age_ent.place(x=275, y=140)

location_ent = Entry(root.left, width=30)
location_ent.place(x=275, y=220)

time_ent = Entry(root.left, width=30)
time_ent.place(x=275, y=260)

phone_ent = Entry(root.left, width=30)
phone_ent.place(x=275, y=300)

delete_box_ent = Entry(root.left, width=30 )
delete_box_ent.place(x=190, y=430)


submit_btn = Button(root.left, text="Add Appointment", width=20, height=2, cursor="hand2", bg='steelblue', command=submit)
submit_btn.place(x=190, y=350)

submit_btn = Button(root.left, text="Update Appointment", width=20, height=2, cursor="hand2", bg='steelblue',command=edit)
submit_btn.place(x=190, y=470)

delete_btn = Button(root.left, text="Delete Appointment", width=20, height=2, cursor="hand2", bg='steelblue', command=delete)
delete_btn.place(x=190, y=550)

submit_btn = Button(root.left, text="logout", width=10, height=1, cursor="hand2", bg='steelblue', command=logout)
submit_btn.place(x=240, y=630)

root.mainloop()
