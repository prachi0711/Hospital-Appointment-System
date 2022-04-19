from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import pymysql

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#6accbc")

        #===Left Image===
        self.left=ImageTk.PhotoImage(file="C:\\Users\\prachi\\Documents\\project\\images\\1.png")
        bg=Label(self.root,image=self.left).place(x=220,y=190,width=300,height=360)
        #=====Login Frame====
        login_frame=Frame(self.root,bg="#99ffff")
        login_frame.place(x=520,y=190,width=550,height=360)

        title=Label(login_frame,text="L O G I N", font=("times new roman",25,"bold"),bg="#99ffff",fg="blue").place(x=50,y=30)

        email=Label(login_frame,text="Email Address", font=("times new roman",15,"bold"),bg="#99ffff",fg="red").place(x=50,y=100)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="white")
        self.txt_email.place(x=50,y=130,width=350,height=35)
        password=Label(login_frame,text="Password", font=("times new roman",15,"bold"),bg="#99ffff",fg="red").place(x=50,y=170)
        self.txt_password=Entry(login_frame,font=("times new roman",15),bg="white")
        self.txt_password.place(x=50,y=200,width=350,height=35)

        btn_reg=Button(login_frame,text="Register new account?",command=self.register_window, fg="#B00857", bg="#99ffff", bd=0, font=("times new roman",12), cursor="hand2").place(x=255,y=240)
        btn_reg=Button(login_frame,text="forget password?",command=self.forgot_password_window, fg="#B00857", bg="#99ffff", bd=0, font=("times new roman",12), cursor="hand2").place(x=285,y=265)
        btn_login=Button(login_frame, text="LOGIN",command=self.login, fg="white", bg="green", font=("times new roman",12,"bold"), cursor="hand2").place(x=50,y=300,width=250)
    def reset(self):
        self.cmb_question.current(0)
        self.txt_password1.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_email.delete(0,END)

    def forget_password(self):
        
        if self.cmb_question.get()=="Select" or self.txt_answer.get()=="" or self.txt_password1.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="management")
                cur=con.cursor()
                cur.execute("select * from appointment where email=%s and question=%s and answer=%s",(self.txt_email.get(),self.cmb_question.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                   messagebox.showerror("Error","Please Select the correct Security Question / Enter Answer", parent=self.root2) 
                   
                else:
                    cur.execute("update appointment set password=%s where email=%s",(self.txt_password1.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your password has been reset, Please login with new password",parent=self.root2)
                    
                    self.reset()
                    self.root2.destroy()
                    

            except Exception as es:
                messagebox.showerror("error",f"Error Due to: {str(es)}",parent=self.root)
                
    def forgot_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter a email address to reset your password", parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="management")
                cur=con.cursor()
                cur.execute("select * from appointment where email=%s",self.txt_email.get())
                row=cur.fetchone()
                if row==None:
                   messagebox.showerror("Error","Please enter a valid email address to reset your password", parent=self.root) 
                   
                else:
                    
                    con.close() 
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x500+950+130")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    j=0
                    r=0
                    for i in range(35):
                        c=str(222222+r)
                        self.bg=Frame(self.root2,width=10,height=500,bg='#'+c).place(x=j,y=0)
                        j=j+10
                        r=r+1

                        Frame(self.root2,width=250,height=400,bg='white').place(x=40,y=40)
                        
                        #label
                        l0=Label(self.root2,text="Forget Password",bg="white",font=('times new roman',18,"bold"),fg="#0033ff")
                        l0.place(x=80,y=60)
                        #label 1
                        question=Label(self.root2,text="security question", font=("times new roman",15),bg="white").place(x=80,y=130)
                        
                        self.cmb_question=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly',justify=CENTER)
                        self.cmb_question['values']=("select","Your pet name","Your best friend name","Your favourite food")
                        self.cmb_question.place(x=80,y=170,width=180)
                        self.cmb_question.current(0)

                        answer=Label(self.root2,text="Your Answer", font=("times new roman",15),bg="white",bd=0).place(x=80,y=200)
                        self.txt_answer=Entry(self.root2,width=30,border=0)
                        self.txt_answer.place(x=80,y=230)

                        

                #label 2
                        password1=Label(self.root2,text='New Password',font=("times new roman",15),bg='white',bd=0).place(x=80,y=280)
                        self.txt_password1=Entry(self.root2,width=30,border=0)
                        self.txt_password1.place(x=80,y=310)
                        
                        

                        
                        Frame(self.root2,width=180,height=2,bg="#141414").place(x=80,y=250)
                        Frame(self.root2,width=180,height=2,bg="#141414").place(x=80,y=330)



                        Button(self.root2,width=20,height=2,fg="white",bg="#994422",border=0,text="Reset Password",command=self.forget_password,cursor="hand2").place(x=100,y=375)

                    
                   
            except Exception as es:
                messagebox.showerror("error",f"Error Due to: {str(es)}",parent=self.root)


    def register_window(self):
        self.root.destroy()
        import register
    
    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("error","All feilds are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="management")
                cur=con.cursor()
                cur.execute("select * from appointment where email=%s and password=%s",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone()
                if row==None:
                   messagebox.showerror("error","Invalid USERNAME & PASSWORD",parent=self.root) 
                   
                else:
                   messagebox.showinfo("Success","Welcome",parent=self.root) 

                   self.root.destroy()
                   import hospitals
                con.close()
                   
            except Exception as es:
                messagebox.showerror("error",f"Error Due to: {str(es)}",parent=self.root)


root=Tk()
obj=Login(root)
root.mainloop()

