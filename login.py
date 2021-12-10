from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from time import strftime
from datetime import datetime
import tkinter
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

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

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
#first image
        img=Image.open(r"F:\projects\ml\college_images\Stanford.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
#second image
        img1=Image.open(r"F:\projects\ml\college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
#third image
        img2=Image.open(r"F:\projects\ml\college_images\u.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

#background Image
        img3=Image.open(r"F:\projects\ml\college_images\bg.jpg")
        img3=img3.resize((1500,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1500,height=790)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM!", font=("times new roman",35,"bold"),bg="white", fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=35)

        #TIME------
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=("times new roman",15,"bold"),background="white",foreground="red")
        lbl.place(x=0,y=0,width=110,height=50)
        time()

#student button
        img4=Image.open(r"F:\projects\ml\college_images\student-portal_1.jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_link,cursor="hand2")
        b1.place(x=100,y=80,width=220,height=220)


#DETECT FACE button
        img5=Image.open(r"F:\projects\ml\college_images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=80,width=220,height=220)


#ATTENDANCE FACE button
        img6=Image.open(r"F:\projects\ml\college_images\imgref3_orig.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=80,width=220,height=220)

#HELP DESK button
        img7=Image.open(r"F:\projects\ml\college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,command=self.help_data,cursor="hand2")
        b1.place(x=1000,y=80,width=220,height=220)

#TRAIN MOdel button
        img8=Image.open(r"F:\projects\ml\college_images\face_detector1.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,command=self.train_data,cursor="hand2")
        b1.place(x=1000,y=320,width=220,height=220)

#PHOTOS button
        img9=Image.open(r"F:\projects\ml\college_images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2")
        b1.place(x=700,y=320,width=220,height=220)

#DEVELOPER BUTTON
        img10=Image.open(r"F:\projects\ml\college_images\Team-Management-Software-Development.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,command=self.Developer_data,cursor="hand2")
        b1.place(x=400,y=320,width=220,height=220)

#EXIT Button
        img11=Image.open(r"F:\projects\ml\college_images\exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=100,y=320,width=220,height=220)

    def open_img(self):
        os.startfile("DATA")

#Exit BUTTON Working
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure You want to exit the application?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

        #-------------------------------------------------FUNCTIONS BUTTONS------------------------------------#
#--------STUDENT DATA BUTTTON-----------------#
    def student_link(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

#--------TRAIN DATA BUTTTON-----------------#
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

#--------FACE RECOGNITION DATA BUTTTON-----------------#
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

#--------ATTENDANCE BUTTTON-----------------#
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

#---------DEVELOPER BUTTON------------------#
    def Developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

#----------HELP BUTTON---------------------#
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


if __name__=='__main__':
    main()
