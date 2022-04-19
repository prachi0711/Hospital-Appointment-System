import tkinter
from tkinter import*
root = Tk()
root.title("Physicians")
Label(root,text="Physicians",font="arial 32",bg="#6accbc").place(x=570,y=80)
def p1():
    root.destroy()
    import demo
def p2():
    root.destroy()
    import demo
def p3():
    root.destroy()
    import demo
l13=Label(root,text="Hospital Name: Shraddha Hospital\n Address: Mahavir Chamber, 24, Bulakhidas Rd, Hira Jain Society, Abu Street Society, Sabarmati, Ahmedabad, Gujarat 380005\n Contact no: 9426389674\n Timings: 10:00 am - 1:00 pm", bg="#6accbc",font="arial 12").place(x=240,y=170)
b1=Button(root, cursor="hand2", text="Book", command=p1).place(x=550,y=260,width=250)
l14=Label(root,text="Hospital name: Care & Cure Clinic \n Address: 21, Subhashnagar, Nr. Bank Of Baroda, Girdhar Nagar, Ahmedabad, Gujarat 380004\n Contact no: 9726297254\n Timings: 9:00 am - 2:00 pm | 5:00 pm - 8:00 pm ", bg="#6accbc",font="arial 12").place(x=350,y=350)
b1=Button(root, cursor="hand2", text="Book", command=p2).place(x=550,y=440,width=250)
l15=Label(root,text="Hospital name: CIMS Hospital\n Address: Sola Gam Rd, Science City, Panchamrut Bunglows II, Sola, Ahmedabad, Gujarat 380060\n Contact no: 9825066664\n Timings: Open 24 hours", bg="#6accbc",font="arial 12").place(x=320,y=510)
b1=Button(root, cursor="hand2", text="Book", command=p3).place(x=550,y=600,width=250)
root.geometry("1350x700+0+0")
root.config(bg="#6accbc")
root.mainloop()