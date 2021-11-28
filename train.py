from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATASET", font=("times new roman",35,"bold"),bg="white" ,anchor="center", fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=35)

#Top Image
        img_top=Image.open(r"F:\projects\ml\college_images\facialrecognition.png")
        img_top=img_top.resize((1400,300),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1400,height=300)

        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="blue",fg="white")
        b1_1.place(x=0,y=365,width=1400,height=40)

#Button ImageTk
        img_bottom=Image.open(r"F:\projects\ml\college_images\facialrecognition.png")
        img_bottom=img_top.resize((1400,250),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=420,width=1400,height=250)


    def train_classifier(self):
        data_dir=("DATA")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #GRAYSCALE Image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #--------------------------------------------Train The classifier and Save-------------------------------------#
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")




if __name__=='__main__':
    root=Tk()
    obj=Train(root)
    root.mainloop()
