from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Page")
        self.root.geometry("1600x900+0+0")


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
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.txt_fname=ttk.Entry(frame,font=("times new roman",15))
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #====================ROW2
        contact=Label(frame,text="How to Contact?",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email Please",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #================ROW3
        security_Q=Label(frame,text="Security Question:",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select your Choice!","Your Birth Place","Any Pet?","Your Favourite Actor")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer?",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)




if __name__=='__main__':
    root=Tk()
    obj=Register(root)
    root.mainloop()
