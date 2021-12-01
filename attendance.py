from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")
#first Image
        img_top=Image.open(r"F:\projects\ml\college_images\smart-attendance.jpg")
        img_top=img_top.resize((800,200),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=600,height=200)

#second image
        img_bottom=Image.open(r"F:\projects\ml\college_images\AdobeStock_303989091.jpeg")
        img_bottom=img_bottom.resize((800,600),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=600,y=0,width=800,height=200)

#background image
        img3=Image.open(r"F:\projects\ml\college_images\face_detector1.jpg")
        img3=img3.resize((1530,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=700)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="white" ,anchor="center", fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=35)

#main FRAME
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=45,width=1450,height=600)

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=500)


if __name__=='__main__':
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
