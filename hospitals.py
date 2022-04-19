import tkinter  
from tkinter import *
from PIL import Image, ImageTk

class female:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.root.title("Hospitals")
       
        self.image=ImageTk.PhotoImage(Image.open("C:\\Users\\prachi\\Documents\\project\\images\\hallway-g726dca513_1920 (1).jpg"))
        canvas=Canvas(self.root,width=1350,height=700)

        canvas.create_image(0,0,anchor=NW,image=self.image)
        canvas.pack()



        self.image1=ImageTk.PhotoImage(file="C:\\Users\\prachi\\Documents\\project\\images\\eye.jpg")
        bg=Label(self.root,image=self.image1).place(x=10,y=100,height=100,width=100)

        self.image2=ImageTk.PhotoImage(file="C:\\Users\\prachi\\Documents\\project\\images\\skin.jpg")
        bg=Label(self.root,image=self.image2).place(x=10,y=220,height=100,width=100)

        self.image3=ImageTk.PhotoImage(file="C:\\Users\\prachi\\Documents\\project\\images\\gyn.jpg")
        bg=Label(self.root,image=self.image3).place(x=10,y=340,height=100,width=100)

        self.image4=ImageTk.PhotoImage(file="C:\\Users\\prachi\\Documents\\project\\images\\orth.jpg")
        bg=Label(self.root,image=self.image4).place(x=10,y=460,height=100,width=100)

        self.image5=ImageTk.PhotoImage(file="C:\\Users\\prachi\\Documents\\project\\images\\phy.jpg")
        bg=Label(self.root,image=self.image5).place(x=10,y=580,height=100,width=100)

        Label(self.root,text="Hospitals", font="arial 32").place(x=550,y=30,width=250)
        
        def tab1():
            import eye 
        b=Button(root, text="Ophthalmologist",cursor="hand2", command=tab1).place(x=150,y=130,width=250)
        def tab2():
            import Dermatologist
        b3=Button(root, text="Dermatologist",cursor="hand2", command=tab2).place(x=150,y=260,width=250)
        def tab3():
            import gynaecologist
        b4=Button(root, text="Gynaecologist",cursor="hand2", command=tab3).place(x=150,y=380,width=250)
        def tab4():
            import orthopedic
        b5=Button(root, text="Orthopaedic",cursor="hand2", command=tab4).place(x=150,y=500,width=250)
        def tab5():
            import Physician
        b6=Button(root, text="Physicians",cursor="hand2", command=tab5).place(x=150,y=620,width=250)
        def app():
            import chatgui

        b7=Button(self.root, text="help",font='arial 12',cursor="hand2", command=app).place(x=1200,y=620,width=80)

    

root = Tk()
obj=female(root)
root.mainloop()
