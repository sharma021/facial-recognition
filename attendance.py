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
        img_bg=Image.open(r"F:\projects\ml\college_images\face_detector1.jpg")
        img_bg=img_bg.resize((1530,700),Image.ANTIALIAS)
        self.photoimg_bg=ImageTk.PhotoImage(img_bg)
        bg_img=Label(self.root,image=self.photoimg_bg)
        bg_img.place(x=0,y=200,width=1530,height=700)



if __name__=='__main__':
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
