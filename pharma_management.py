from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

def main():
        win=Tk()
        app=Login_window(win)
        win.mainloop()


class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0")
        
        self.bg=ImageTk.PhotoImage(file=r"C:\\Users\\Admin\\Desktop\\numpy\\pharma\\bg2.jpg")
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open("C:\\Users\\Admin\\Desktop\\numpy\\pharma\\logo_page.png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS) 
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
#for the Name
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=98,y=100)

#create label  and entry for input
        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=188,width=270)


        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

#for icon images
        img2=Image.open("C:\\Users\\Admin\\Desktop\\numpy\\pharma\\logo_page.png")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=328,width=25,height=25)



        img3=Image.open("C:\\Users\\Admin\\Desktop\\numpy\\pharma\\password.png")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25)

#Login button
        loginbtn=Button(frame,text="Login",command=self.Login_System,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

#Registration button
        registerbtn=Button(frame,text="NewUser Register",command=self.register_window,borderwidth=0,font=("times new roman",10,"bold"),fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

#forgetpass button
        forgetpassbtn=Button(frame,text="Forget Password",command=self.Forget_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetpassbtn.place(x=10,y=370,width=160)


#We work on login button

    def Login_System (self):
        if  self.txtuser.get()=="" or  self.txtpass.get()=="":
            messagebox.showerror("Error","all fields are requried")
        elif self.txtuser.get()=="Sumit" and  self.txtpass.get()=="1234" :
            messagebox.showinfo("Succes")

        else:
            conn=mysql.connector.connect(
                                    host="localhost",
                                    username="root",
                                    password="Sumit@1209",
                                    database="quantizer" )

            my_cursor=conn.cursor()
            my_cursor.execute("select* from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))

            row=my_cursor.fetchone()

            #print

            if row==None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Acces only admin")
                if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=PharmaMangementSystem(self.new_window)
                
                else:
                        if not open_main:
                                return
            conn.commit()
            conn.close
#=============================================work on forget password===============================
# create forget password mysql server and create reseat password page 
    def Forget_password_window (self):
        if  self.txtuser.get()=="":
                messagebox.showerror("error","please write email address for reset password")
        else:
                conn=mysql.connector.connect(host="localhost",
                                    username="root",
                                    password="Sumit@1209",
                                    database="quantizer" )
                my_cursor=conn.cursor()
                query=("select * from register where email=%s")
                value=(self.txtuser.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                print(row)

                if row==None:
                        messagebox.showerror("My Error","Please fill valid-user name") 
                else:
                        conn.close()
                        self.root2=Toplevel()
                        self.root2.title("forget password")
                        self.root2.geometry("1500x800+0+0")
        
                        self.bg1=ImageTk.PhotoImage(file=r"C:\\Users\\Admin\\Desktop\\numpy\\pharma\\bg2.jpg")
                        lb1_bg1=Label(self.root2,image=self.bg)
                        lb1_bg1.place(x=0,y=0,relwidth=1,relheight=1)
                        

                        frame2=Frame(self.root2,bg="brown",bd=15,relief=RIDGE)
                        frame2.place(x=610,y=300,width=340,height=450)


                        l=Label(frame2,text="Reset Password",font=("times new roman",25,"bold"),bg="black",fg="Red")
                        l.place(x=0,y=10,relwidth=1)

                        

                        

                        security_Q=Label(frame2,text="Select Security Question",font=("times new roman",15,"bold"),bg="brown",fg="black")
                        security_Q.place(x=40,y=80)
        
                        self.combo_security_Q=ttk.Combobox(frame2,font=("times new roman",15,"bold"),state="readonly")
                        self.combo_security_Q["values"]=("Select","Your Birth Place","Your girlfriend name","your Pet Name")
                        self.combo_security_Q.place(x=40,y=110,width=250)
                        self.combo_security_Q.current(0)




                        security_A=Label(frame2,text="Security Answer",font=("times new roman",15,"bold"),bg="brown",fg="black")
                        security_A.place(x=40,y=150)

                        self.txt_security=ttk.Entry(frame2,font=("times new roman",15,"bold"))
                        self.txt_security.place(x=40,y=180,width=250)

                        new_password=Label(frame2,text="New Password",font=("times new roman",15,"bold"),bg="brown",fg="black")
                        new_password.place(x=40,y=220)

                        self.txt_newpass=ttk.Entry(frame2,font=("times new roman",15,"bold"))
                        self.txt_newpass.place(x=40,y=250,width=250)


                        button_1=Button(frame2,text="Reset",command=self.reset_pass,font=("arail",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
                        button_1.place(x=40,y=300,width=120,height=35)

                        button_2=Button(frame2,text="Sign In",command=self.Exit_data2,font=("arail",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
                        button_2.place(x=160,y=300,width=120,height=35)


# work on reset button
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
                messagebox.showerror("Error","Select Security Question",parent=self.root2)
        
        if self.txt_security.get()=="Select":
                messagebox.showerror("Error","Please enter a answer",parent=self.root2)
        
        if self.txt_newpass.get()=="Select":
                messagebox.showerror("Error","Please enter a New password",parent=self.root2)

        else:
                conn=mysql.connector.connect(host="localhost",
                                    username="root",
                                    password="Sumit@1209",
                                    database="quantizer" )
                my_cursor=conn.cursor()
                query=("select * from register where email=%s and securityQ=%s and securityA=%s ")
                value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
                my_cursor.execute(query,value)

                row=my_cursor.fetchone()
                print(row)

                if row==None:
                        messagebox.showerror("Error","Please Enter correct password ",parent=self.root2)
                else:
                        query=("update register set password=%s where email=%s")
                        value=(self.txt_newpass.get(),self.txtuser.get())
                        my_cursor.execute(query,value)

                        conn.commit()
                        conn.close()
                        messagebox.showinfo("info","your password is set, plz login with new password",parent=self.root2)
# for the login page
    def Exit_data2(self):
        Exit_data2=messagebox.askyesno("Reset password","conform you want to go login page",parent=self.root2)
        if Exit_data2>0:
                self.root2.destroy()
                return
  






                




# for open the registration form , 
# open the registration form in the new registrion button on the login page
    def register_window(self):
        self.new_window=Toplevel(self.root)   #toplevel is the pre build fuction in tkinter
        self.app=Register(self.new_window)



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0")


#============================variable which is used in declaation in entry and function,method================================
        self.var_fname =StringVar()
        self.var_lname =StringVar()
        self.var_contact =StringVar()
        self.var_email =StringVar()
        self.var_securityQ =StringVar()
        self.var_SecurityA =StringVar()
        self.var_pass =StringVar()
        self.var_confpass =StringVar()
        self.var_check =IntVar()


        
        self.bg=ImageTk.PhotoImage(file=r"C:\\Users\\Admin\\Desktop\\numpy\\pharma\\reBg4.jpg")
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0,relwidth=1,relheight=1)
    
        self.bg1=ImageTk.PhotoImage(file=r"C:\\Users\\Admin\\Desktop\\numpy\\pharma\\Releftside.jpg")
        lb1_bg1=Label(self.root,image=self.bg1)
        lb1_bg1.place(x=50,y=100,width=470,height=550)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
#======================registration label+++++++++++++
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green")
        register_lbl.place(x=20,y=20)

#+========================label and Entry================================
        #1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

#2
        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

#3
        contact=Label(frame,text="Contact",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)
#4


        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)
#5
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your girlfriend name","your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)



#6
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security_A=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15,"bold"))
        self.txt_security_A.place(x=370,y=270,width=250)
#7


        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)
#8

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

#9
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the term and condition",font=("times new roman",15,"bold"),bg="white")
        checkbtn.place(x=50,y=390)

#10
 #       b1=Button(frame,text="Register Now",bg="red",fg="blue",font=("times new roman",12,"bold"),cursor="hand2")
 #       b1.place(x=50,y=450,width=100)

        self.icon1=ImageTk.PhotoImage(file=r"C:\\Users\\Admin\\Desktop\\numpy\\pharma\\register-button-png-18466.jpg")
        lb1_icon1=Button(frame,command=self.register_data,image=self.icon1,borderwidth=0,bg="white",cursor="hand2")
        lb1_icon1.place(x=50,y=450,width=200)

#11

    #    b1=Button(frame,text="Login Now",bg="red",fg="blue",font=("times new roman",12,"bold"),cursor="hand2")
    #    b1.place(x=250,y=450,width=100)
     
        self.icon2=ImageTk.PhotoImage(file=r"C:\\Users\\Admin\\Desktop\\numpy\\pharma\\login-button-png-18030.png")
        lb1_icon2=Button(frame,image=self.icon2,bg="white",borderwidth=0,cursor="hand2",command=self.Exit_data3)
        lb1_icon2.place(x=450,y=450,width=200)

#===============================================Decleration of function=====================================================================
        
    def register_data(self):
            if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                    messagebox.showerror("Please check detail","All fields are required",parent=self.root)

            elif self.var_pass.get()!=self.var_confpass.get():
                        messagebox.showerror("Please check detail","Passwored and confirm passwored should be same",parent=self.root)

            elif self.var_check.get()==0:
                    messagebox.showerror("Please check detail","please agree our term and Condition",parent=self.root)

            else:
                conn=mysql.connector.connect(
                                    host="localhost",
                                    username="root",
                                    password="Sumit@1209",
                                    database="quantizer" )

                my_cursor=conn.cursor()
                query=("select * from register where email=%s")
                value=(self.var_email.get(),)   
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                if row!=None:
                        messagebox.showerror("Error","User already exist,please try another email",parent=self.root)

                else:
                        my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_fname.get(),
                                                                                                self.var_lname.get(),
                                                                                                self.var_contact.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_securityQ.get(),
                                                                                                self.var_SecurityA.get(),
                                                                                                self.var_pass.get()
                                                                                                ))

                conn.commit()
                conn.close()
                messagebox.showinfo("Succes","Welcome, your Registration is succesfull",parent=self.root)
      
    def Exit_data3(self):
        #Exit_data3=messagebox.askyesno("Reset password","conform you want to go login page",parent=self.root)
        #if Exit_data3>0:
                self.root.destroy()
                return
  

   
 
# open pharamcy in login page
class PharmaMangementSystem:
    def __init__(self,root):
        self.root=root                                  #varaible
        self.root.title("PHARMACY MANAGEMNT SYSTEM")
        self.root.geometry("1550x800+0+0")
#--------------------------variable uses in add medicine right side------------------------------
        self.refMed_var=StringVar()                     #000
        self.AddMed_var=StringVar()                     #000

#--------------------------variable uses in main data  medicine information left side------------------------------
        self.ref_var=StringVar()           #1.11111
        self.cmpName_var=StringVar()
        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideeffect_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()


        lbtitle=Label(self.root,text="Pharma Mangement System",bd=15,relief=RIDGE,bg="red",fg="darkgreen",font=("times new roman",50,"bold"),padx=2,pady=4)
        lbtitle.pack(fill=X)
#--------------------Images in LAble upper-----------------------------------------------
        img1=Image.open("C:\\Users\\Admin\\Desktop\\numpy\pharma\\logos.jpg")
        img1=img1.resize((80,80),Image.Resampling.LANCZOS)   #covert high resize of pic to low
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=20)
#---------------------Data Frame-----------------------------
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1530,height=400)
#---------------------Data Frame Left-----------------------------
        DataFrameLeft=LabelFrame(DataFrame,text="Medicine Information",bd=10,relief=RIDGE,padx=20,fg="darkgreen")
        DataFrameLeft.place(x=0,y=5,width=900,height=350)
#---------------------Data Frame Left-----------------------------
        DataFrameRight=LabelFrame(DataFrame, text="Medicine Add Deparment",bd=10,relief=RIDGE,padx=20,fg="darkgreen")
        DataFrameRight.place(x=910,y=5,width=540,height=350)
#---------------------buttons Frame-----------------------------
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE)
        ButtonFrame.place(x=0,y=520,width=1530,height=65)

#---------------------button formation-----------------------------
        btnaddData=Button(ButtonFrame,command=self.add_data,text="Medicine Add",width=13,font=("arial",12,"bold"),bg="darkgreen",fg="white")
        btnaddData.grid(row=0,column=0)
        btnUpdateMed=Button(ButtonFrame,command=self.Update,text="Update",width=13,font=("arial",13,"bold"),bg="darkgreen",fg="white")    #10.102
        btnUpdateMed.grid(row=0,column=1)
        btnDeleteMed=Button(ButtonFrame,command=self.Delete,text="Delete",width=13,font=("arial",13,"bold"),bg="red",fg="white")
        btnDeleteMed.grid(row=0,column=2)
        btnrestMed=Button(ButtonFrame,command=self.Reset,text="Reset",width=13,font=("arial",13,"bold"),bg="darkgreen",fg="white")
        btnrestMed.grid(row=0,column=3)
        btnExitMed=Button(ButtonFrame,command=self.Exit_data,text="Exit",width=13,font=("arial",13,"bold"),bg="darkgreen",fg="white")
        btnExitMed.grid(row=0,column=4)
#---------------------search button formation-----------------------------
        IblSearch=Label(ButtonFrame,text="search by",bg="red",fg="white",font=("arial",15,"bold"))
        IblSearch.grid(row=0,column=5,sticky=W)

        #variable store in combobox  #13.102
        self.search_var=StringVar()

        

#---------------------button formation-----------------------------combobox for the combox we import ttk from tkinter
        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=13,font=("arrail",17,"bold"))  #13.103
        search_combo["values"]=("Ref_no","MedName","LotNo")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

#---------------------entry formation-----------------------------
         #variable store in Entry   #13.104
        self.searchText_var=StringVar()
       
        
        txtSerch=Entry(ButtonFrame,textvariable=self.searchText_var,bd=3,relief=RIDGE,width=13,font=("arrail",17,"bold"))     #13.105
        
        txtSerch.grid(row=0,column=7)
#---------------------search formation--------------------------r
        seaechBtn=Button(ButtonFrame,command=self.search_data,text="Search",width=13,font=("arial",12,"bold"),bg="darkgreen",fg="white")
        seaechBtn.grid(row=0,column=8)
        
        showAll=Button(ButtonFrame,command=self.fetch_data,text="Show all",width=13,font=("arial",12,"bold"),bg="darkgreen",fg="white")
        showAll.grid(row=0,column=9)
#--------------------create level and entry in -Data Frame left sided-----------------------------
#1
        lbrefno=Label(DataFrameLeft, font=("arial",12,"bold"),text="Referance no",padx=2)
        lbrefno.grid(row=0,column=0,sticky=W)

        # create connection in DataframeLeft side at refernace no
        conn=mysql.connector.connect(
                                    host="localhost",
                                    username="root",
                                    password="Sumit@1209",
                                    database="quantizer"
        )
        my_cursor=conn.cursor()
        my_cursor.execute("select ref from pharmas")
        row=my_cursor.fetchall()  #1111


        ref_combo=ttk.Combobox(DataFrameLeft,textvariable=self.ref_var, width=27,font=("arial",12,"bold"),state="readonly")
        ref_combo["values"]=row   #1111
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)
#2
        lblcompanyname=Label(DataFrameLeft,font=("arial",12,"bold"),text="Company Name :",padx=2,pady=6)
        lblcompanyname.grid(row=1,column=0,sticky=W)

        txtCompanyName=Entry(DataFrameLeft,textvariable=self.cmpName_var, font=("arrail",13,"bold"),bg="white",bd=3,relief=RIDGE,width=29)
        txtCompanyName.grid(row=1,column=1)
#3
        lbltypeofMedicine=Label(DataFrameLeft, font=("arial",12,"bold"),text="Type Of Medicine",padx=2,pady=6)
        lbltypeofMedicine.grid(row=2,column=0,sticky=W)

        comTypeofMedicine=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var, width=27,font=("arial",12,"bold"),state="readonly")
        comTypeofMedicine["values"]=("Tablets","Liquid","Capusles","Drops","Inheals","Injection")
        comTypeofMedicine.grid(row=2,column=1)
        comTypeofMedicine.current(0)
 #4       
        lbMedicineName=Label(DataFrameLeft, font=("arial",12,"bold"),text="Medicine Name",padx=2,pady=6)
        lbMedicineName.grid(row=3,column=0,sticky=W)
        # create connection in DataframeLeft side at Medicine Name
        conn=mysql.connector.connect(
                                    host="localhost",
                                    username="root",
                                    password="Sumit@1209",
                                    database="quantizer"
        )
        my_cursor=conn.cursor()
        my_cursor.execute("select MedName from pharmas")
        row1=my_cursor.fetchall()

        comMedicineNAme=ttk.Combobox(DataFrameLeft,textvariable=self.medName_var,width=27,font=("arial",12,"bold"),state="readonly")
        comMedicineNAme["values"]=row1
        comMedicineNAme.grid(row=3,column=1)
        comMedicineNAme.current(0)
#5
        lbllotNo=Label(DataFrameLeft, font=("arial",12,"bold"),text="Lot No:",padx=2,pady=6)
        lbllotNo.grid(row=4,column=0,sticky=W)

        txtLotNo=Entry(DataFrameLeft,textvariable=self.lot_var, font=("arrail",13,"bold"),bg="white",bd=3,relief=RIDGE,width=29)
        txtLotNo.grid(row=4,column=1)
#6
        lblIssueDate=Label(DataFrameLeft, font=("arial",12,"bold"),text="Issu Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)

        txtIssuedate=Entry(DataFrameLeft,textvariable=self.issuedate_var,font=("arrail",13,"bold"),bg="white",bd=3,relief=RIDGE,width=29)
        txtIssuedate.grid(row=5,column=1)
#7
        lblExpDate=Label(DataFrameLeft, font=("arial",12,"bold"),text="Exp Date :",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)

        txtExpDate=Entry(DataFrameLeft,textvariable=self.expdate_var,font=("arrail",13,"bold"),bg="white",bd=3,relief=RIDGE,width=29)
        txtExpDate.grid(row=6,column=1)
#8
        lbluses=Label(DataFrameLeft, font=("arial",12,"bold"),text="Uses:",padx=2)
        lbluses.grid(row=7,column=0,sticky=W)

        txtUses=Entry(DataFrameLeft,textvariable=self.uses_var,font=("arrail",13,"bold"),bg="white",bd=3,relief=RIDGE,width=29)
        txtUses.grid(row=7,column=1)
#9
        lblsideEffect=Label(DataFrameLeft, font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblsideEffect.grid(row=8,column=0,sticky=W)

        txtSideEffect=Entry(DataFrameLeft,textvariable=self.sideeffect_var,font=("arrail",13,"bold"),bg="white",bd=3,relief=RIDGE,width=29)
        txtSideEffect.grid(row=8,column=1)
 #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  #10 
        lblPrecWarning=Label(DataFrameLeft, font=("arial",12,"bold"),text="Prec & Warning:",padx=15,pady=6)
        lblPrecWarning.grid(row=0,column=2,sticky=W)
        txtPrecWarning=Entry(DataFrameLeft,textvariable=self.warning_var,font=("arrail",13,"bold"),bg="white",bd=3,relief=RIDGE,width=29)
        txtPrecWarning.grid(row=0,column=3)   
#11
        lblDosage=Label(DataFrameLeft, font=("arial",12,"bold"),text="Dosage:",padx=15,pady=6)
        lblDosage.grid(row=1,column=2,sticky=W)

        txtDosage=Entry(DataFrameLeft,textvariable=self.dosage_var,font=("arrail",13,"bold"),bg="white",bd=3,relief=RIDGE,width=29)
        txtDosage.grid(row=1,column=3)
#12
        lblTabletsPrice=Label(DataFrameLeft, font=("arial",12,"bold"),text="Tablets Price:",padx=15,pady=6)
        lblTabletsPrice.grid(row=2,column=2,sticky=W)

        txtTabletsPrice=Entry(DataFrameLeft,textvariable=self.price_var,font=("arrail",13,"bold"),bg="white",bd=3,relief=RIDGE,width=29)
        txtTabletsPrice.grid(row=2,column=3)
#13
        lblProductQT=Label(DataFrameLeft, font=("arial",12,"bold"),text="Product QT:",padx=15,pady=6)
        lblProductQT.grid(row=3,column=2,sticky=W)

        txtProductQT=Entry(DataFrameLeft,textvariable=self.product_var,font=("arrail",13,"bold"),bg="white",bd=3,relief=RIDGE,width=29)
        txtProductQT.grid(row=3,column=3)
#--------------------create level and entry in -Data Frame left sided-----------------------------   
        img2=Image.open("C:\\Users\\Admin\\Desktop\\numpy\\pharma\\tablet.jpg")
        img2=img2.resize((150,135),Image.Resampling.LANCZOS)   #covert high resize of pic to low
        self.photoimg2=ImageTk.PhotoImage(img2)
        b2=Button(self.root,image=self.photoimg2,borderwidth=0)
        b2.place(x=770,y=330)

        img3=Image.open("C:\\Users\\Admin\\Desktop\\numpy\\pharma\\eng.jpg")
        img3=img3.resize((150,135),Image.Resampling.LANCZOS)   #covert high resize of pic to low
        self.photoimg3=ImageTk.PhotoImage(img3)
        b3=Button(self.root,image=self.photoimg3,borderwidth=0)
        b3.place(x=620,y=330)

        img4=Image.open("C:\\Users\\Admin\\Desktop\\numpy\\pharma\\madam.jpg")
        img4=img4.resize((150,135),Image.Resampling.LANCZOS)   #covert high resize of pic to low
        self.photoimg4=ImageTk.PhotoImage(img4)
        b4=Button(self.root,image=self.photoimg4,borderwidth=0)
        b4.place(x=475,y=330)
     
        lblhome=Label(DataFrameLeft, font=("arial",12,"bold"),text="Stay Home and Stay Safe",padx=2,pady=6,fg="red",width=37)
        lblhome.place(x=410,y=140)

#--------------------create level and entry in -Data Frame Right sided in mobile app development-----------------------------
        img5=Image.open("C:\\Users\\Admin\\Desktop\\numpy\\pharma\\eng.jpg")
        img5=img5.resize((175,75),Image.Resampling.LANCZOS)   #covert high resize of pic to low
        self.photoimg5=ImageTk.PhotoImage(img5)
        b5=Button(self.root,image=self.photoimg5,borderwidth=0)
        b5.place(x=960,y=160)

        img6=Image.open("C:\\Users\\Admin\\Desktop\\numpy\\pharma\\tablet.jpg")
        img6=img6.resize((175,75),Image.Resampling.LANCZOS)   #covert high resize of pic to low
        self.photoimg6=ImageTk.PhotoImage(img6)
        b6=Button(self.root,image=self.photoimg6,borderwidth=0)
        b6.place(x=1130,y=160)


        img7=Image.open("C:\\Users\\Admin\\Desktop\\numpy\\pharma\\madam.jpg")
        img7=img7.resize((200,145),Image.Resampling.LANCZOS)   #covert high resize of pic to low
        self.photoimg7=ImageTk.PhotoImage(img7)
        b7=Button(self.root,image=self.photoimg7,borderwidth=0)
        b7.place(x=1270,y=160)

#-------------------------------Level in Medicine App Department-----------------------------
        lblRefrancenum=Label(DataFrameRight, font=("arial",12,"bold"),text="Reference No :")
        lblRefrancenum.place(x=0,y=80)

        txtRefrancenum=Entry(DataFrameRight ,textvariable=self.refMed_var,font=("arrail",13,"bold")  ,bg="white",bd=3,relief=RIDGE,width=16)    #000
        txtRefrancenum.place(x=135,y=80)
#-------------------------------------------------------------------------------------------------------------------------------

        lblmedName=Label(DataFrameRight, font=("arial",12,"bold"),text="Medicine Name:")
        lblmedName.place(x=0,y=110)

        txtmedName=Entry(DataFrameRight,textvariable=self.AddMed_var,font=("arail",13,"bold"),bg="white",bd=3,relief=RIDGE,width=16)         #000
        txtmedName.place(x=135,y=110)

#---------------------------------Side Frame in  DataFrameRight ----------------------------------------------------------------------------------------------
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="White")
        side_frame.place(x=0,y=150,width=290,height=160)
#---------------------------------IN Side Frame Create Scrollbar  ----------------------------------------------------------------------------------------------
        
        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

#---------------------------------Create TREEview ----------------------------------------------------------------------------------------------
        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview) #learn about config and tree view
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table["show"]="headings"

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")

        
        self.medicine_table.pack(fill=BOTH,expand=1) #learn about fill,expand

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)

        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)       #2222


#------------------------------medicine Add Button in right data frame------------------------------------------------

        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=330,y=155,height=160)

        btnaddmed=Button(down_frame,command=self.AddMed,text="Add",width=12,font=("arial",12,"bold"),bg="lightgreen",fg="white",pady=4,)
        btnaddmed.grid(row=0,column=0)

        btnUpdateMed=Button(down_frame,command=self.UpdateMed,text="Update",width=12,font=("arial",13,"bold"),bg="purple",fg="white",pady=4)
        btnUpdateMed.grid(row=1,column=0)
        
        btnDeleteMed=Button(down_frame,command=self.DeleteMed,text="Delete",width=12,font=("arial",13,"bold"),bg="red",fg="white",pady=4) #444
        btnDeleteMed.grid(row=2,column=0)    
        
        btnClearMed=Button(down_frame,command=self.ClearMed,text="Clear",width=12,font=("arial",13,"bold"),bg="orange",fg="white",pady=4)  #555
        btnClearMed.grid(row=3,column=0)

#------------------------------Create  FrameDetail in page ------------------------------------------------
#1
        frameDetail=Frame(self.root,bd=14,relief=RIDGE,bg="lightgreen")
        frameDetail.place(x=0,y=590,width=1530,height=210)

#------------------------------Create  mainTable and scrollbar in FrameDetail  ------------------------------------------------
#2     
        table_frame=Frame(frameDetail,bd=15,relief=RIDGE)
        table_frame.place(x=0,y=1,width=1500,height=180)
#3
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

#-------------------------create tree view----------------------
#4
        self.pharmacy_table=ttk.Treeview(table_frame,column=("reg","companyname","type","tabletname","lotno","issuedate",
                                                             "expdate","uses","sideeffect","Warning","dosage","price","productqt")
                                                             ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
 #5       
        scroll_x.pack(side="bottom",fill=X)
        scroll_y.pack(side="right",fill=Y)
#6
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)
#=+++============================================================================================================================
#7
        self.pharmacy_table["show"]="headings"

        self.pharmacy_table.heading("reg",text="Reference No")
        self.pharmacy_table.heading("companyname", text=" Company Name ")
        self.pharmacy_table.heading("type", text="Type Of Medicine")
        self.pharmacy_table.heading("tabletname", text="Tablet Name ")
        self.pharmacy_table.heading("lotno", text="Lot No ")
        self.pharmacy_table.heading("issuedate", text="Issue Date ")
        self.pharmacy_table.heading("expdate", text=" Exp Date")
        self.pharmacy_table.heading("uses", text="Uses")
        self.pharmacy_table.heading("sideeffect", text="Side Effect ")
        self.pharmacy_table.heading("Warning", text=" Prec&Warning")
        self.pharmacy_table.heading("dosage", text=" Dosage")
        self.pharmacy_table.heading("price", text="Price ")
        self.pharmacy_table.heading("productqt", text="Product Qts ")
        self.pharmacy_table.pack(fill="both",expand=1)  
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)       #9.92


# we set width of table
        self.pharmacy_table.column("reg",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("Warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)
        self.fetch_dataMed()         # for fetch data in self.medicine table part 3
        self.fetch_data()            #8.83

#                        now we work on Mysql
   # +++++++++++++++++++++++++ add medicine functionality decleration++++++Start+++++++++++++
 # create method 
    def AddMed(self):                   # for use mysql command in button....we command on button and take some variable
        if self.refMed_var.get()==""or self.AddMed_var.get=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
                conn=mysql.connector.connect(
                                            host="localhost",
                                            username="root",
                                            password="Sumit@1209",
                                            database="quantizer"
                )
                my_cursor=conn.cursor()
                my_cursor.execute("insert into pharmas values(%s,%s)",(
                                                                     self.refMed_var.get(),
                                                                     self.AddMed_var.get() 
                                                                     ))

                conn.commit()
                self.fetch_dataMed()      # for fetch data in self.medicine table part 2
                conn.close
                messagebox.showinfo("success","Medicine addes",parent=self.root)
        

    def fetch_dataMed(self):      # for fetch data in self.medicine table part 1
        conn=mysql.connector.connect(
                                    host="localhost",
                                    username="root",
                                    password="Sumit@1209",
                                    database="quantizer"
        )
        my_cursor=conn.cursor()
        my_cursor.execute("select* from pharmas")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.medicine_table.delete(*self.medicine_table.get_children())
                for i in rows:
                     self.medicine_table.insert("",END,values=i)
                conn.commit()
        conn.close()

##=================================with the help of cursor we put the resukt  value from ref and mediciane name into the (level iside the mediction add frame ) =============================================
    def Medget_cursor(self,event=""):              #222
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row3=content["values"]
        self.refMed_var.set(row3[0])
        self.AddMed_var.set(row3[1])

##++++++++++++++++++++++++++++++++++we update the given value+++++++++++++++++++++++++++++++++++++++++++++++++++
    def UpdateMed(self):           #333
        if self.refMed_var.get()==""or self.AddMed_var.get=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
                conn=mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Sumit@1209",
                        database="quantizer"
                )
                my_cursor=conn.cursor()
                my_cursor.execute("update pharmas set MedName=%s where Ref=%s",(
                                                                     
                                                                     self.AddMed_var.get() ,
                                                                     self.refMed_var.get()
                                                                     ))
                


                conn.commit()
                self.fetch_dataMed()
                messagebox.showinfo("Scusses","Medicine has been Updated",parent=self.root)

   

#++++++++++++++++++++++++++++++++++we Delete the given value+++++++++++++++++++++++++++++++++++++++++++++++++++
    def DeleteMed(self):   #444
        conn=mysql.connector.connect(host="localhost",username="root",password="Sumit@1209",database="quantizer")
        my_cursor=conn.cursor()
        sql="delete from pharmas where Ref=%s"
        val=(self.refMed_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_dataMed()
        messagebox.showinfo("Scusses","Medicine has been Deleted",parent=self.root) 

#-----------------------------------we clear the given value in ref and medicine name--------------------------
    def ClearMed(self):   #555
        self.refMed_var.set("")
        self.AddMed_var.set("")

   # +++++++++++++++++++++++++ add medicine functionality decleration++++++END+++++++++++++
##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ data medicine informstion decleration @@@@@@@@ start @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
    def add_data(self):              #1.11111
        conn=mysql.connector.connect(host="localhost",username="root",password="Sumit@1209",database="quantizer")
        my_cursor=conn.cursor()

        my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                           self.ref_var.get() ,                                                             
                                                                                           self.cmpName_var.get(),
                                                                                           self.typeMed_var.get(),
                                                                                           self.medName_var.get(),
                                                                                           self.lot_var.get(),
                                                                                           self.issuedate_var.get(),
                                                                                           self.expdate_var.get(),
                                                                                           self.uses_var.get(),
                                                                                           self.sideeffect_var.get(),
                                                                                           self.warning_var.get(),
                                                                                           self.dosage_var.get(),
                                                                                           self.price_var.get(),
                                                                                           self.product_var.get()
        ))
        conn.commit()
        self.fetch_data()         #8.82
        self.fetch_dataMed()      # for fetch data in self.medicine table part 2
        conn.close
        messagebox.showinfo("success","Medicine addes",parent=self.root)


    def fetch_data(self):      #8.81    # for fetch data in pharmacy_table part 1
        conn=mysql.connector.connect(                    
                                    host="localhost",
                                    username="root",
                                    password="Sumit@1209",
                                    database="quantizer"
        )
        my_cursor=conn.cursor()
        my_cursor.execute("select* from pharmacy")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                for i in rows:
                     self.pharmacy_table.insert("",END,values=i)
                conn.commit()
        conn.close()




    def get_cursor(self,event=""):             #9.91
        cursor_row=self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row4=content["values"]
       
        self.ref_var.set(row4[0]) ,                                                             
        self.cmpName_var.set(row4[1]),
        self.typeMed_var.set(row4[2]),
        self.medName_var.set(row4[3]),
        self.lot_var.set(row4[4]),
        self.issuedate_var.set(row4[5]),
        self.expdate_var.set(row4[6]),
        self.uses_var.set(row4[7]),
        self.sideeffect_var.set(row4[8]),
        self.warning_var.set(row4[9]),
        self.dosage_var.set(row4[10]),
        self.price_var.set(row4[11]),
        self.product_var.set(row4[12])



    def Update(self):           #10.101
        if self.ref_var.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
                conn=mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Sumit@1209",
                        database="quantizer"
                )
                my_cursor=conn.cursor()   
                my_cursor.execute("update pharmacy set CmpName=%s,TypeMed=%s,MedName=%s,LotNo=%s,Issuedate=%s,Expdate=%s,Uses=%s,Sideeffect=%s,warning=%s,dosage=%s,Price=%s,Product=%s where Ref_no=%s",(
                                                                     
                                                                                                                                                    
                                                                                           self.cmpName_var.get(),
                                                                                           self.typeMed_var.get(),
                                                                                           self.medName_var.get(),
                                                                                           self.lot_var.get(),
                                                                                           self.issuedate_var.get(),
                                                                                           self.expdate_var.get(),
                                                                                           self.uses_var.get(),
                                                                                           self.sideeffect_var.get(),
                                                                                           self.warning_var.get(),
                                                                                           self.dosage_var.get(),
                                                                                           self.price_var.get(),
                                                                                           self.product_var.get(),
                                                                                           self.ref_var.get() 
                                                                                           ))
                conn.commit()
                self.fetch_dataMed()
                messagebox.showinfo("Scusses","Medicine has been Updated",parent=self.root)

    def Delete(self):  #11.101
        conn=mysql.connector.connect(host="localhost",username="root",password="Sumit@1209",database="quantizer")
        my_cursor=conn.cursor()
        sql="delete from pharmacy where Ref_no=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_data()
        messagebox.showinfo("Scusses","Medicine has been Deleted",parent=self.root)

    def Reset(self):   #12.101
       self.ref_var.set("") ,                                                             
       self.cmpName_var.set(""),
       self.typeMed_var.set(""),
       self.medName_var.set(""),
       self.lot_var.set(""),
       self.issuedate_var.set(""),
       self.expdate_var.set(""),
       self.uses_var.set(""),
       self.sideeffect_var.set(""),
       self.warning_var.set(""),
       self.dosage_var.set(""),
       self.price_var.set(""),
       self.product_var.set("")



    def search_data(self):    #13.101
        conn=mysql.connector.connect(host="localhost",username="root",password="Sumit@1209",database="quantizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy where %s LIKE %s",(
                self.search_var.get(),
                self.searchText_var.get(),

        ))
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                          
                for i in rows:
                     self.pharmacy_table.insert("",END,values=i)
                conn.commit()
                

        
        conn.close()
        messagebox.showinfo("succues","search button work",parent=self.root)

    def Exit_data(self):
        Exit_data=messagebox.askyesno("Pharma Managment System","conform you want to exist",parent=self.root)
        if Exit_data>0:
                self.root.destroy()
                return
 




if __name__=="__main__":
    main()

