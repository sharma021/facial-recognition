from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


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
        registerbtn=Button(frame,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="red")
        registerbtn.place(x=20,y=350,width=120)

        #Forget password Button
        forgetpassbtn=Button(frame,text="Forget password",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="red")
        forgetpassbtn.place(x=20,y=370,width=120)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error!","All Fields are Required!")
        elif self.txtuser.get()=="vidu" and self.txtpass.get()=="anshu":
            messagebox.showinfo("Success!","Welcome To V Snap!!")
        else:
            messagebox.showerror("Invalid","Invalid username and password!")



if __name__=='__main__':
    root=Tk()
    obj=Login_Window(root)
    root.mainloop()
