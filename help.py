from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

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

        



if __name__=='__main__':
    root=Tk()
    obj=Help(root)
    root.mainloop()
