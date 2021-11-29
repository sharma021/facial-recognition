from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition

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

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=700,y=80,width=220,height=220)

#HELP DESK button
        img7=Image.open(r"F:\projects\ml\college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
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

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=400,y=320,width=220,height=220)

#EXIT Button
        img11=Image.open(r"F:\projects\ml\college_images\exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=100,y=320,width=220,height=220)

    def open_img(self):
        os.startfile("DATA")

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



if __name__=='__main__':
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
