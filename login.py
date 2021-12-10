from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"F:\projects\ml\college_images\hackers2.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=520,y=170,width=340,height=450)

        img1=Image.open(r"F:\projects\ml\college_images\di.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=175,width=100,height=100)

        get_str=Label(frame,text="WELCOME STUDENT!",font=("times new roman",15,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #Label
        username=lbl=Label(frame,text="USERNAME",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=100,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="PASSWORD",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=100,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #-------------------Icon Images------------------#
        img2=Image.open(r"F:\projects\ml\college_images\di.jpg")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=580,y=323,width=25,height=25)

        img3=Image.open(r"F:\projects\ml\college_images\di.jpg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=580,y=393,width=25,height=25)

        #LOGIN BUTTON
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=120,y=300,width=120,height=35)

        #Register Button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="red")
        registerbtn.place(x=20,y=350,width=120)


        #Forget password Button
        forgetpassbtn=Button(frame,text="Forget password",command=self.forget_password_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="red")
        forgetpassbtn.place(x=20,y=370,width=120)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error!","All Fields are Required!")
        elif self.txtuser.get()=="vidu" and self.txtpass.get()=="anshu":
            messagebox.showinfo("Success!","Welcome To V Snap!!")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sql-password",database="userdata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                    ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Invalid","Invalid username and password!")
            else:
                open_main=messagebox.askyesno("yes/No","Acess only admin")
                if open_main>0:
                    self.new_window=Toplevel()
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
    #=================================Reset password=======================================#

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error!","Select Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error!","Please first answer the QUESTION",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Enter a new password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sql-password",database="userdata")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,vlue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error!","Sorry,Wrong answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("information","Password updated successfully!",parent=self.root2)
                self.root2.destroy()




    #=================================Forget window========================================#
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error!","Please first enter the email address to reset the password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sql-password",database="userdata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            #print ROW
            if row==None:
                messagebox.showerror("Error friend","PLease enter a valid email address")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                register_lbl=Label(self.root2,text="RESET YOUR PASSWORD!!",font=("times new roman",15,"bold"),fg="darkgreen",bg="white")
                register_lbl.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Security Question:",font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select your Choice!","Your Birth Place","Any Pet?","Your Favourite Actor")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer?",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="Choose a new password!",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                #Reset button1
                btn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)






class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Page")
        self.root.geometry("1600x900+0+0")

        #================VARIABLES================#
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        #background Image
        self.bg=ImageTk.PhotoImage(file=r"F:\projects\ml\college_images\hackers2.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        #left Image
        self.bg1=ImageTk.PhotoImage(file=r"F:\projects\ml\college_images\Stanford.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",15,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #=============================LABEL AND ENTRY============================#

        #================ROW1
        fname=Label(frame,text="What to call you?",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.txt_fname=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #====================ROW2
        contact=Label(frame,text="How to Contact?",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email Please",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #================ROW3
        security_Q=Label(frame,text="Security Question:",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select your Choice!","Your Birth Place","Any Pet?","Your Favourite Actor")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer?",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #===================ROW4

        pswd=Label(frame,text="Set a password",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=315)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=345,width=250)

        confirm_pswd=Label(frame,text="Confirm the password",font=("times new roman",15,"bold"),bg="white")
        confirm_pswd.place(x=370,y=315)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=345,width=250)

        #=====================Checkbutton
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree to the terms and conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=385)

        #=========================BUTTONS
        img=Image.open(r"F:\projects\ml\college_images\register-now-button1.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.Photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.Photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=20,y=415,width=250)

        img2=Image.open(r"F:\projects\ml\college_images\loginpng.png")
        img2=img2.resize((200,50),Image.ANTIALIAS)
        self.Photoimage2=ImageTk.PhotoImage(img2)
        b1=Button(frame,image=self.Photoimage2,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=280,y=415,width=250)

#============================Function Declaration==================================#
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error!!","All the details are mandatory")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error Again!","Looks like the password and the confirm password details are not the same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error!","First agree to our terms and conditions!")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sql-password",database="userdata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error!","User with same email already exists","please use another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success Message","Congratulations!, successfully Registered")

if __name__=='__main__':
    main()
