import tkinter
from tkinter import*
root = Tk()
root.title("Dermatologist")
Label(root,text="Dermatologist",font="arial 32",bg="#6accbc").place(x=550,y=80)
def booking():
    root.destroy()
    import demo
def booking1():
    root.destroy()
    import demo
def booking2():
    root.destroy()
    import demo
l4=Label(root,text="Hospital Name: Lumos Skinic\n Address: 536, Yash Arian, Memnagar Rd, Bhuyangdev Society, Memnagar, Ahmedabad, Gujarat 380052\n Timings: 10:00 am - 8:00 pm\n Contact no: 7227010908",bg="#6accbc",font="arial 12").place(x=320,y=170)
b1=Button(root, cursor="hand2", text="Book", command=booking).place(x=550,y=260,width=250)
l5=Label(root,text="Hospital name: Aashtha Skin Care and Lazer Clinic\n Address:F-7 ,shubh complex, near Rajasthan Hospital Ahmedabad, Shahibag, Ahmedabad, Gujarat 380004\n Contact no: 9898183828\n Timings: 11:00 am - 6:00 pm",bg="#6accbc",font="arial 12").place(x=320,y=350)
b1=Button(root, cursor="hand2", text="Book", command=booking1).place(x=550,y=440,width=250)
l6=Label(root,text="Hospital name: Angel Skin Hair Lazer Clinic\n Address: C-403 Hometown - 5 Besides S.V Square mall, New Ranip, Ahmedabad, Gujarat 382470 \n Contact no: 9099040705\n Timings: 10:00 am - 5:30 pm",bg="#6accbc",font="arial 12").place(x=320,y=510)
b1=Button(root, cursor="hand2", text="Book", command=booking2).place(x=550,y=600,width=250)
root.geometry("1350x700+0+0")
root.config(bg="#6accbc")
root.mainloop()