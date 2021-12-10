from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER", font=("times new roman",35,"bold"),bg="white" ,anchor="center", fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=35)
#BACK BUTTON
        Back_Button=Button(self.root,text="Back",command=self.root.destroy,font=("arial",11,"bold"),width=17,bg="white",fg="red")
        Back_Button.pack(side=LEFT)
        Back_Button.place(x=0,y=20)

#Top Image
        img_top=Image.open(r"F:\projects\ml\college_images\dev.jpg")
        img_top=img_top.resize((1400,600),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1400,height=600)

        #FRAME
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=902,y=0,width=450,height=500)

        img_top1=Image.open(r"F:\projects\ml\college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top1=img_top1.resize((200,300),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=150,height=150)

        #DEVELOPER Information
        dev_label=Label(main_frame,text="Hello! I am Vidya Sharma", font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=1,y=5)

        dev_label=Label(main_frame,text="I am an Information Technology Student", font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=30)

        #Image
        img2=Image.open(r"F:\projects\ml\college_images\Stanford.jpg")
        img2=img2.resize((500,300),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=200,width=500,height=300)



if __name__=='__main__':
    root=Tk()
    obj=Developer(root)
    root.mainloop()
