import tkinter
from tkinter import*
root = Tk()
root.title("Gynaecologist")
Label(root,text="Gynaecologist",font="arial 32", bg="#6accbc").place(x=550,y=80)
def r1():
    root.destroy()
    import demo
def r2():
    root.destroy()
    import demo
def r3():
    root.destroy()
    import demo
l7=Label(root,text="Hospital Name: Sneh Maternity Hospital\n Address: SNEH PLAZA COMPLEX FIRST FLOOR, IOC Rd, Chandkheda, Ahmedabad, Gujarat 382424 \n Contact no: 9408863878 \n Timings: Open 24 hours", bg="#6accbc",font="arial 12").place(x=350,y=170)
b1=Button(root, cursor="hand2", text="Book", command=r1).place(x=550,y=260,width=250)
l8=Label(root,text="Hospital name: Mamta Hospital\n Address: A-5, Jal Vihar Flats, Ashram Road, Bh Ajanta Commercial Centre, Ashram Road, Ahmedabad, Gujarat 380014\n Contact no: 07927540918\n Timings: Open 24 hours", bg="#6accbc",font="arial 12").place(x=270,y=350)
b1=Button(root, cursor="hand2", text="Book", command=r2).place(x=550,y=440,width=250)
l9=Label(root,text="Hospital name: Jeevandeep Hospital\n Address: 1 & 2,1st Floor, Sopan Complex near AMTS bus stop, Sabarmati, Ahmedabad, Gujarat 382424 \n Contact no: 9825289409\n Timings: 9:30 am - 12:30 pm | 5:30 - 7:30 ", bg="#6accbc",font="arial 12").place(x=330,y=510)
b1=Button(root, cursor="hand2", text="Book", command=r3).place(x=550,y=600,width=250)
root.geometry("1350x700+0+0")
root.config(bg="#6accbc")
root.mainloop()