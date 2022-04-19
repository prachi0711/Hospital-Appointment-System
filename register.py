from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import pymysql

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#6accbc")
        #===Bg Image===
        self.bg=ImageTk.PhotoImage(file="C:\\Users\\prachi\\Documents\\project\\images\\2.png")
        bg=Label(self.root,image=self.bg).place(x=20,y=0,relwidth=1,relheight=1)

        #===Left Image===
        self.left=ImageTk.PhotoImage(file="C:\\Users\\prachi\\Documents\\project\\images\\1.png")
        bg=Label(self.root,image=self.left).place(x=180,y=100,width=300,height=530)

        #=====Register Frame====
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=530)
        
        title=Label(frame1,text="Register Here", font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        #-----ro1
        
        f_name=Label(frame1,text="First Name", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)
        l_name=Label(frame1,text="Last Name", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)


        #------row2
        contact=Label(frame1,text="Contact Number", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        email_name=Label(frame1,text="Email", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)
        #------ row3
        question=Label(frame1,text="security question", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        
        self.cmb_question=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_question['values']=("select","Your pet name","Your best friend name","Your favourite food")
        self.cmb_question.place(x=50,y=270,width=250)
        self.cmb_question.current(0)

        answer=Label(frame1,text="Your Answer", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)


        #-------row4
        password=Label(frame1,text="Password", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)
        confirmpassword=Label(frame1,text="Confirm Password", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_confirmpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_confirmpassword.place(x=370,y=340,width=250)
        #-----terms and conditions
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white", font=("times new roman", 12)).place(x=50,y=380)

        btn_register=Button(frame1, text="Register", fg="white", bg="green", font=("times new roman",12,"bold"), cursor="hand2",command=self.register_data).place(x=50,y=420,width=180)
        btn_login=Button(self.root, text="Login",command=self.login_window, fg="black", bg="white", font=("times new roman",12,"bold"), cursor="hand2").place(x=230,y=520,width=200)
    def login_window(self):
        self.root.destroy()
        import login3
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_confirmpassword.delete(0,END)
        self.txt_answer.delete(0,END)
        self.cmb_question.current(0)
    
    

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_question.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_confirmpassword.get()=="":
            messagebox.showerror("Error","All Feilds Are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_confirmpassword.get():
            messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions",parent=self.root)

        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="management")
                cur=con.cursor()
                cur.execute("select * from appointment where email=%s",self.txt_email.get())
                row=cur.fetchone()
                
                if row!=None:
                    messagebox.showerror("Error","User already exist, Please Try with another email",parent=self.root)
                else:
                    cur.execute("insert into appointment (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                   (self.txt_fname.get(),
                                   self.txt_lname.get(),
                                   self.txt_contact.get(),
                                   self.txt_email.get(),
                                   self.cmb_question.get(),
                                   self.txt_answer.get(),
                                   self.txt_password.get()
                                   ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registration Successful",parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"error due to: {str(es)}",parent=self.root)
            

root=Tk()
obj=Register(root)
root.mainloop()
