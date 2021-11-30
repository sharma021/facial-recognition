from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        title_lbl=Label(self.root,text="FACE RECOGNITION", font=("times new roman",35,"bold"),bg="white" ,anchor="center", fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=35)

#Left Image
        img_top=Image.open(r"F:\projects\ml\college_images\face_detector1.jpg")
        img_top=img_top.resize((550,600),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=550,height=600)

#right image
        img_bottom=Image.open(r"F:\projects\ml\college_images\detect.jpg")
        img_bottom=img_bottom.resize((900,600),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=550,y=50,width=900,height=600)

        #button
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="blue",fg="white")
        b1_1.place(x=350,y=525,width=200,height=40)

#----------------------------------ATTENDANCE----------------------------------------#

    def mark_attendance(self,l,k,i,j):
        with open("attend.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((" , "))
                name_list.append(entry[0])
            if((l not in name_list) and (k not in name_list) and (i not in name_list) and (j not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{l},{k},{i},{j},{dtString},{d1},Present")




#---------------------------------FACE RECOGNITION-----------------------------------#
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="sql-password",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select Name from student where Student_id= "+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select Dep from student where Student_id= "+str(id))
                j=my_cursor.fetchone()
                j="+".join(j)

                my_cursor.execute("select RollNO from student where Student_id= "+str(id))
                k=my_cursor.fetchone()
                k="+".join(k)

                my_cursor.execute("select Student_id from student where Student_id= "+str(id))
                l=my_cursor.fetchone()
                l="+".join(l)

                if confidence>77:
                    cv2.putText(img,f"ID:{l}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{k}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{j}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(l,k,i,j)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("WELCOME TO FACE RECOGNITION!!",img)


            if cv2.waitKey(500):
                break
            video_cap.release()
            cv2.destroyAllWindows()

if __name__=='__main__':
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
