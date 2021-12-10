from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")


#---------------------------------------Variables-----------------------------------#
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
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
        
#BACK BUTTON
        Back_Button=Button(bg_img,text="Back",command=self.root.destroy,font=("arial",11,"bold"),width=17,bg="white",fg="red")
        Back_Button.pack(side=LEFT)
        Back_Button.place(x=0,y=0)

#main FRAME
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=45,width=1450,height=600)

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=430)

        img_left=Image.open(r"F:\projects\ml\college_images\face_detector1.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=10,y=135,width=640,height=300)

        #labeland Entry
        #attendance ID
        attendanceId_label=Label(left_inside_frame,relief=RIDGE,text="Student ID", font=("conicsansns 11 bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("conicsansns 11 bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Roll lABEL
        Roll_label=Label(left_inside_frame,relief=RIDGE,text="Roll No", font=("conicsansns 11 bold"),bg="white")
        Roll_label.grid(row=0,column=2,padx=4,pady=8,sticky=W)

        atten_label_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("conicsansns 11 bold"))
        atten_label_entry.grid(row=0,column=3,padx=8,pady=5,sticky=W)

        #Name
        name_label=Label(left_inside_frame,relief=RIDGE,text="Name", font=("conicsansns 11 bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        attten_name_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("conicsansns 11 bold"))
        attten_name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Department
        dep_label=Label(left_inside_frame,relief=RIDGE,text="Department", font=("conicsansns 11 bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        depl_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("conicsansns 11 bold"))
        depl_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

#Date
        dep_label=Label(left_inside_frame,relief=RIDGE,text="Date", font=("conicsansns 11 bold"),bg="white")
        dep_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        depl_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("conicsansns 11 bold"))
        depl_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


#Time
        time_label=Label(left_inside_frame,relief=RIDGE,text="Time", font=("conicsansns 11 bold"),bg="white")
        time_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        T_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("conicsansns 11 bold"))
        T_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #attendance PhotoSampleStatus
        attendancelabel=Label(left_inside_frame,text="Attendance Status",bg="white",font="comicsansns 11 bold")
        attendancelabel.grid(row=3,column=0)
        self.atten_status=ttk.Combobox(left_inside_frame,width=20,font="conicsansns 11 bold", state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=650,height=60)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=15,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #right label frame
        RIGHT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        RIGHT_frame.place(x=680,y=10,width=660,height=430)

        table_frame=Frame(RIGHT_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=650,height=380)

        #Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","Department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance id")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance Status")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=110)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
#-----------------------------------------------FETCH DATA-----------------------------------------#
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

#import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

#export csvread
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Erro",f"Due to :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")



if __name__=='__main__':
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
