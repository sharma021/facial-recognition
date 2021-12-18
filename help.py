import cv2
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import webbrowser



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()

        title_lbl=Label(self.root,text="Your Problem, Our Problem!", font=("times new roman",20,"bold"),bg="white" ,anchor="center", fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=35)

#BACK BUTTON
        Back_Button=Button(self.root,text="Back",command=self.root.destroy,font=("arial",11,"bold"),width=17,bg="white",fg="red")
        Back_Button.pack(side=LEFT)
        Back_Button.place(x=0,y=20)



#Top Image
        img_top=Image.open(r"F:\projects\ml\college_images\iStock-1163542789-945x630.jpg")
        img_top=img_top.resize((1400,600),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1400,height=600)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=0,y=95,width=1400,height=400)

        img_left=Image.open(r"F:\projects\ml\facial recognition system\file photos\help.jpg")
        img_left=img_left.resize((500,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(main_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=550,height=400)

        register_lbl=Label(main_frame,text="RAISE A TOKEN!",font=("times new roman",15,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=550,y=20)

        fname=Label(main_frame,text="Your Name Please",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=560,y=60)

        self.txt_fname=ttk.Entry(main_frame,textvariable=self.var_fname,font=("times new roman",15))
        self.txt_fname.place(x=750,y=60,width=250)

        l_name=Label(main_frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        l_name.place(x=560,y=100)

        self.txt_lname=ttk.Entry(main_frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=750,y=100,width=250)

        #====================ROW2
        contact=Label(main_frame,text="How to Contact?",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=560,y=140)

        self.txt_contact=ttk.Entry(main_frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=750,y=140,width=250)

        email=Label(main_frame,text="Your issue?",font=("times new roman",15,"bold"),bg="white")
        email.place(x=560,y=180)

        self.txt_email=ttk.Entry(main_frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=750,y=180,width=250)

        img=Image.open(r"F:\projects\ml\facial recognition system\file photos\submit.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.Photoimage=ImageTk.PhotoImage(img)
        b1=Button(main_frame,image=self.Photoimage,command=self.submit_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=560,y=240,width=250)

        extra_lbl=Label(main_frame,text="Or you can contact below!",font=("times new roman",15,"bold"),fg="darkgreen",bg="white")
        extra_lbl.place(x=550,y=300)

        web_Button=Button(main_frame,text="LINKEDIN",command=self.web_browser,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        web_Button.place(x=560,y=340)
        insta_Button=Button(main_frame,text="INSTAGRAM",command=self.insta_browser,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        insta_Button.place(x=820,y=340)

        TWITTER_Button=Button(main_frame,text="TWITTER",command=self.TWITTER_browser,font=("arial",11,"bold"),width=17,bg="BLUE",fg="white")
        TWITTER_Button.place(x=1100,y=340)
    def web_browser(self):
        webbrowser.open("https://www.linkedin.com/in/vidya-sharma-328757167/")
    def insta_browser(self):
        webbrowser.open("https://drive.google.com/file/d/15M87_2-L2aTIv8An1LvWcK_lO0Wfi0Ec/view")
    def TWITTER_browser(self):
        webbrowser.open("https://twitter.com/VidyaSharma021")



    def submit_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error!!","All the details are mandatory")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sql-password",database="userdata")
            my_cursor=conn.cursor()
            query=("select * from help where Contact=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error!","User with same email already exists","please use another email")
            else:
                my_cursor.execute("insert into help values(%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),

                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success Message","We got your Message, we will get back to you soon")


if __name__=='__main__':
    root=Tk()
    obj=Help(root)
    root.mainloop()
