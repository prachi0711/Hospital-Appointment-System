import tkinter
from tkinter import*
root = Tk()
root.title("Eye Hospitals")
Label(root,text="Eye Hospitals",font="arial 32", bg="#6accbc").place(x=550,y=80)
def books():
    root.destroy()
    import demo
def books1():
    root.destroy()
    import demo
def books2():
    root.destroy()
    import demo
l1=Label(root,text="Hospital Name: Eyeconic Eye Clinic\n Address: 405-406, Mehta 531, Outside VS Hospital, Ellis Bridge, Ahmedabad-380006\n Timings: 5:00 pm - 8:00 pm\n Contact no: 7947161234", bg="#6accbc",font="arial 12").place(x=380,y=170)
b1=Button(root, cursor="hand2", text="Book", command=books).place(x=550,y=260,width=250)
l2=Label(root,text="Hospital name: Divyadrashti Eye Clinic\n Address: 401, Emporio Complex, Opposite 4D Square Mall, Motera, Ahmedabad-380005\n Contact no:7947068402\n Timings: 10:00 am - 1:00 pm | 5:00 pm - 7:30 pm", bg="#6accbc",font="arial 12").place(x=380,y=350)
b1=Button(root, cursor="hand2", text="Book", command=books1).place(x=550,y=440,width=250)
l3=Label(root,text="Hospital name: Aneri Eye Hospital\n Address: 3, Vasantkunj, New Sharda Mandir Road, Paldi, Ahmedabad-380007\n Contact no: 7926606370\n Timings:10:00 am - 1:00 pm | 5:00 pm - 7:30 pm", bg="#6accbc",font="arial 12").place(x=380,y=510)
b1=Button(root, cursor="hand2", text="Book", command=books2).place(x=550,y=600,width=250)
root.geometry("1350x700+0+0")
root.config(bg="#6accbc")
root.mainloop()