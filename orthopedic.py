import tkinter
from tkinter import*
root = Tk()
root.title("Orthopaedics")
Label(root,text="Orthopaedics",font="arial 32" ,bg="#6accbc").place(x=550,y=80)
def book():
    root.destroy()
    import demo
def book1():
    root.destroy()
    import demo
def book2():
    root.destroy()
    import demo
l10=Label(root,text="Hospital Name: Auroma Orthopaedics Hospital \n Address: 2nd Floor, Shashwat Complex, Swastik Cross Rd, Naranpura, Ahmedabad, Gujarat 380013 \n Contact no: 8347810098 \n Timings: 4:30 pm - 6:30 pm",  bg="#6accbc",font="arial 12").place(x=350,y=170)
b1=Button(root, cursor="hand2", text="Book", command=book).place(x=550,y=260,width=250)
l11=Label(root,text="Hospital name: Samarth Orthopedic Hospital\n Address: SF1 & 2, Aakar complex,11,Nathalal colony Above Parul Lab, Sardar Patel Stadium Rd, Navrangpura, Ahmedabad, Gujarat 380014\n Contact no: 9099989697\n Timings: Open 24 hours",  bg="#6accbc",font="arial 12").place(x=220,y=350)
b1=Button(root, cursor="hand2", text="Book", command=book1).place(x=550,y=440,width=250)
l12=Label(root,text="Hospital name: Aneri Hospital \n Address: Simandhar Sthapak, 2nd, opposite ladli showroom, Naranpura, Ahmedabad, Gujarat 380013\n Contact no: 07927435430\n Timings: 10:00 am - 1:00 pm | 6:00 pm - 7:30 pm",  bg="#6accbc",font="arial 12").place(x=320,y=510)
b1=Button(root, cursor="hand2", text="Book", command=book2).place(x=550,y=600,width=250)
root.geometry("1350x700+0+0")
root.config(bg="#6accbc")
root.mainloop()