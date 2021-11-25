from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        #---------------------------Variables--------------------------#
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

#first image
        img=Image.open(r"F:\projects\ml\college_images\AdobeStock_303989091.jpeg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
#second image
        img1=Image.open(r"F:\projects\ml\college_images\face-recognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        #third image

        img2=Image.open(r"F:\projects\ml\college_images\facial-recognition_0.jpg")
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

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("arial",30,"bold"),bg="white", fg="dark green",anchor="center")
        title_lbl.place(x=0,y=0,width=1530,height=35)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=45,width=1450,height=800)


        #left label Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=500)
        #image in left frame
        img_left=Image.open(r"F:\projects\ml\college_images\gettyimages-1022573162.jpg")
        img_left=img_left.resize((500,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=7,y=0,width=650,height=100)

        #CURRENT COURSE FRAME
        course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Course Information",font=("times new roman",12,"bold"))
        course_frame.place(x=5,y=100,width=650,height=100)

        #Departmentlabel
        dep_label=Label(course_frame,relief=RIDGE,text="Department",font=("times new roman",11,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        #Department Combobox
        dep_combo=ttk.Combobox(course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=15,state="readonly")
        dep_combo['values']=("Select Department","CSE","ITE","ECE","MECH","EEE","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1)

        #COURSE
        course_label=Label(course_frame,relief=RIDGE,text="Course", font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=15)
        course_combo['values']=("Select Course","BE","ME","DIPLOMA","B.Tech","M.Tech")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,sticky=W)


        #YEAR
        year_label=Label(course_frame,relief=RIDGE,text="Year", font=("times new roman",12,"bold"),bg="white",anchor="center")
        year_label.grid(row=1,column=0)

        year_combo=ttk.Combobox(course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=15,)
        year_combo['values']=("Select Year",1,2,3,4)
        year_combo.current(0)
        year_combo.grid(row=1,column=1,sticky=W)

        #SEMESTER
        sem_label=Label(course_frame,relief=RIDGE,text="Semester", font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,sticky=W)

        sem_combo=ttk.Combobox(course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=15)
        sem_combo['values']=("Select Semester",1,2,3,4,5,6,7,8)
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,sticky=W)

        #Class Student Information
        Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        Student_frame.place(x=5,y=180,width=650,height=280)

        #Student Label
        sid_label=Label(Student_frame,relief=RIDGE,text="Student ID", font=("times new roman",12,"bold"),bg="white")
        sid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        sid_entry=Entry(Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        sid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student __name_
        studname_label=Label(Student_frame,relief=RIDGE,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studname_label_entry=Entry(Student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        studname_label_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Class Division
        class_div_label=Label(Student_frame,relief=RIDGE,text="Class Division",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #class_div_label_entry=Entry(Student_frame,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
        #class_div_label_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        class_div_combo=ttk.Combobox(Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=15,state="readonly")
        class_div_combo['values']=("Select Division","A","B","C","D")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll No.
        Roll_label=Label(Student_frame,relief=RIDGE,text="Roll No.",font=("times new roman",12,"bold"),bg="white")
        Roll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Roll_label_entry=Entry(Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        Roll_label_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #Email
        Email_label=Label(Student_frame,relief=RIDGE,text="Email",font=("times new roman",12,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Email_label_entry=Entry(Student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        Email_label_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone No.
        Phone_label=Label(Student_frame,relief=RIDGE,text="Contact",font=("times new roman",12,"bold"),bg="white")
        Phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        Phone_label_entry=Entry(Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        Phone_label_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        Address_label=Label(Student_frame,relief=RIDGE,text="Gender",font=("times new roman",12,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        #Address_label_entry=Entry(Student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        #Address_label_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        Address_combo=ttk.Combobox(Student_frame,textvariable=self.var_address,font=("times new roman",12,"bold"),width=15,state="readonly")
        Address_combo['values']=("Select Gender","Male","Female","Other")
        Address_combo.current(0)
        Address_combo.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher Name
        teach_label=Label(Student_frame,relief=RIDGE,text="DOB",font=("times new roman",12,"bold"),bg="white")
        teach_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teach_label_entry=Entry(Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teach_label_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        #radio buttons
        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(Student_frame,variable=self.var_radio2,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)

        #buttons frame
        btn_frame=Frame(Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=170,width=650,height=60)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=200,width=650,height=45)

        takephoto_btn=Button(btn_frame1,text="Take Photo Sample",width=32,font=("times new roman",13,"bold"),bg="blue",fg="white")
        takephoto_btn.grid(row=0,column=0)

        Updatephoto_btn=Button(btn_frame1,text="Update Photo Sample",width=32,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Updatephoto_btn.grid(row=0,column=1)


        #Right label Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=660,height=500)

        img_right=Image.open(r"F:\projects\ml\college_images\AdobeStock_303989091.jpeg")
        img_right=img_right.resize((500,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=650,height=100)

        ################# SEARCH SYSTEM ############################

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=100,width=650,height=72)

        #SEARCH LABEL
        search_label=Label(Search_frame,relief=RIDGE,text="Search By", font=("times new roman",12,"bold"),bg="gray")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),width=10,state="readonly")
        search_combo['values']=("Select", "Roll No.", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=14,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(Search_frame,text="Show All",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)

        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=170,width=650,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.stud_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","dob","roll","gender","phone","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.stud_table.xview)
        scroll_y.config(command=self.stud_table.yview)

        self.stud_table.heading("dep",text="Department")
        self.stud_table.heading("course",text="Course")
        self.stud_table.heading("year",text="Year")
        self.stud_table.heading("sem",text="Semester")
        self.stud_table.heading("id",text="Student_id")
        self.stud_table.heading("name",text="Name")
        self.stud_table.heading("dob",text="DOB")
        self.stud_table.heading("roll",text="Roll No")
        self.stud_table.heading("gender",text="Gender")
        self.stud_table.heading("phone",text="Contact")

        self.stud_table.heading("photo",text="PhotoSampleStatus")
        self.stud_table["show"]="headings"

        self.stud_table.column("dep",width=100)
        self.stud_table.column("course",width=100)
        self.stud_table.column("year",width=100)
        self.stud_table.column("sem",width=100)
        self.stud_table.column("id",width=100)
        self.stud_table.column("name",width=100)
        self.stud_table.column("dob",width=100)
        self.stud_table.column("roll",width=100)
        self.stud_table.column("gender",width=100)
        self.stud_table.column("phone",width=100)
        self.stud_table.column("photo",width=115)
        self.stud_table.pack(fill=BOTH,expand=1)
        self.stud_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

#=================================Function Declaration=====================#
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sql-password",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_semester.get(),
                                                                                                    self.var_std_id.get(),
                                                                                                    self.var_name.get(),
                                                                                                    self.var_div.get(),
                                                                                                    self.var_roll.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_teacher.get(),
                                                                                                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}", parent=self.root)

        #-------------------------------------------------FETCH DATA------------------------------------#
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sql-password",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.stud_table.delete(*self.stud_table.get_children())
            for i in data:
                self.stud_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        #----------------------------------------GET CURSOR Function---------------------------------#
    def get_cursor(self,event=""):
        cursor_focus=self.stud_table.focus()
        content=self.stud_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_address.set(data[10]),
        self.var_teacher.set(data[11]),
        self.var_radio1.set(data[12])


#Update Function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details?",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="sql-password",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,RollNO=%s,Email=%s,Gender=%s,Contact=%s,DOB=%s,photosample=%s where Student_id=%s",(
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_std_id.get()
                                                                                                                                                                        ))
                else:
                    if not update:
                        return
                    messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="sql-password",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

#Reset Function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set(" ")
        self.var_name.set(" ")
        self.var_div.set("Select Division")
        self.var_roll.set(" ")
        self.var_email.set(" ")
        self.var_phone.set(" ")
        self.var_address.set("Male")
        self.var_teacher.set(" ")
        self.var_radio1.set()












if __name__=='__main__':
    root=Tk()
    obj=Student(root)
    root.mainloop()
