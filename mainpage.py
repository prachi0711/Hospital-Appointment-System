from tkinter import *
from PIL import Image, ImageTk

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Main Page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.bg=ImageTk.PhotoImage(file="C:\\Users\\prachi\\Documents\\project\\images\\medical-gec4a5f141_1920.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,height=700,width=1350)

        self.left=ImageTk.PhotoImage(file="C:\\Users\\prachi\\Documents\\project\\images\\1641820299682 (1).jpg")
        bg=Label(self.root,image=self.left).place(x=10,y=0,height=150,width=150)

        title=Label(self.root,text="WELCOME TO HOSPITAL APPOINTMENT", font=("times new roman",35,"bold"),fg="blue").place(x=230,y=250)

        btn_login=Button(self.root, text="login as user", fg="black",border="5",command=self.user_login, font=("times new roman",12,"bold"), cursor="hand2").place(x=380,y=370,width=250)
        btn_login=Button(self.root, text="login as doctor", fg="black",border="5",command=self.doctor_login, font=("times new roman",12,"bold"), cursor="hand2").place(x=700,y=370,width=250)
    def user_login(self):
        self.root.destroy()
        import login3
    
    def doctor_login(self):
        self.root.destroy()
        import doctor_login
    
root=Tk()
obj=Login(root)
root.mainloop()

