#front end
from tkinter import *
import tkinter.messagebox, tkinter.filedialog as filedialog
import project1_backend as pb
import csv
import os
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
import configparser
config = configparser.ConfigParser()

mydata=[]


class Student:
    
    def __init__(self,root):
       self.root=root 
       self.root.title("student database management system")
       self.root.geometry(newGeometry="1150x600+0+0")
       self.root.config(bg="#E7E3E2")
       #ASSIGN SOME VARIABLE TO STORE OUR ENTRY FILELD VALUES
       stdId=StringVar()
       Firstname=StringVar()
       Surname=StringVar()
       DoB=StringVar()
       Age=StringVar()
       Gender=StringVar()
       Adress=StringVar()
       Mobile=StringVar()
       Marks=StringVar()
       config = configparser.ConfigParser()
       config.read('configfile.ini')
       viewKey=[]
       viewValue=[]
       for key in config['view']:
       	viewValue.append(config['view'][key])
       	viewKey.append(key)
       	
       ###########################FUNCTIONS#############
       pb.studentData()
       def iExit():
              iExit=tkinter.messagebox.askyesno("Priyanka's student dbms","conform if you want to exit")
              if iExit>0:
                     root.destroy()
                     return
       def clearData():
              
              self.txtStdId.delete(0,END)
              if(viewValue[0].lower()=='yes'):
              		self.txtFirstname.delete(0,END)
              if(viewValue[1].lower()=='yes'):
              		self.txtSurname.delete(0,END)
              if(viewValue[2].lower()=='yes'):
              		self.txtDob.delete(0,END)
              if(viewValue[3].lower()=='yes'):
              		self.txtAge.delete(0,END)
              if(viewValue[4].lower()=='yes'):
              		self.txtGender.delete(0,END)
              if(viewValue[5].lower()=='yes'):
              		self.txtAdress.delete(0,END)
              if(viewValue[6].lower()=='yes'):
              		self.txtMobile.delete(0,END)
              if(viewValue[7].lower()=='yes'):
              		self.txtMarks.delete(0,END) 
       
       pb.studentData()             
       def addData():
              if(len(stdId.get())!=0):
                     
                     lock=pb.addStdRec(stdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Adress.get(),Mobile.get(),Marks.get())
                     if lock==0:
                     	showinfo(title='Information', message='Record alredy exist')
                     studentlist.delete(0,END)
                     studentlist.insert(END,(stdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Adress.get(),Mobile.get(),Marks.get()))
                     clearData()
                     DisplayData()

       def DisplayData():
              #print(viewKey)
              studentlist.delete(0,END)
              for item in tree.get_children():
              	tree.delete(item)
              for row in pb.viewData():
              		#print(row)
              		A=[row[0]]
              		if(viewValue[0].lower()=='yes'):
              			A.append(row[1])
              		if(viewValue[1].lower()=='yes'):
              			A.append(row[2])
              		if(viewValue[2].lower()=='yes'):
              			A.append(row[3])
              		if(viewValue[3].lower()=='yes'):
              			A.append(row[4])
              		if(viewValue[4].lower()=='yes'):
              			A.append(row[5])
              		if(viewValue[5].lower()=='yes'):
              			A.append(row[6])
              		if(viewValue[6].lower()=='yes'):
              			A.append(row[7])
              		if(viewValue[7].lower()=='yes'):
              			A.append(row[8])
              		studentlist.insert(END,row)
              		tree.insert('', END, values=A)
              
       def item_selected(event):
       	global record
       	for selected_item in tree.selection():
       		item = tree.item(selected_item)
       		record = item['values']
       		n=len(viewValue)
       		count=0
       		ll=0
       		for i in range(n):
       			if(viewValue[0].lower()=='yes'):
       				count=count+1
       		
       		self.txtStdId.delete(0,END)
       		self.txtStdId.insert(END,record[0])
       		if(viewValue[0].lower()=='yes'):
	       		self.txtFirstname.delete(0,END)
	       		self.txtFirstname.insert(END,record[1])
	       	else:
	       		ll+=1
       		if(viewValue[1].lower()=='yes'):
	       		self.txtSurname.delete(0,END)
	       		self.txtSurname.insert(END,record[2-ll])
	       	else:
	       		ll+=1
       		if(viewValue[2].lower()=='yes'):
	       		self.txtDob.delete(0,END)
	       		self.txtDob.insert(END,record[3-ll])
	       	else:
	       		ll+=1
       		if(viewValue[3].lower()=='yes'):
	       		self.txtAge.delete(0,END)
	       		self.txtAge.insert(END,record[4-ll])
	       	else:
	       		ll+=1
       		if(viewValue[4].lower()=='yes'):
	       		self.txtGender.delete(0,END)
	       		self.txtGender.insert(END,record[5-ll])
	       	else:
	       		ll+=1
       		if(viewValue[5].lower()=='yes'):
	       		self.txtAdress.delete(0,END)
	       		self.txtAdress.insert(END,record[6-ll])
	       	else:
	       		ll+=1
       		if(viewValue[6].lower()=='yes'):
	       		self.txtMobile.delete(0,END)  
	       		self.txtMobile.insert(END,record[7-ll])
	       	else:
	       		ll+=1
       		if(viewValue[7].lower()=='yes'):
	       		self.txtMarks.delete(0,END)  
	       		self.txtMarks.insert(END,record[8-ll])     
       		
       def StudentRec(event):
              global sd
              searchstd = studentlist.curselection()[0]
              sd=studentlist.get(searchstd)
              self.txtStdId.delete(0,END)
              self.txtStdId.insert(END,sd[0])
              self.txtFirstname.delete(0,END)
              self.txtFirstname.insert(END,sd[1])
              self.txtSurname.delete(0,END)
              self.txtSurname.insert(END,sd[2])
              self.txtDob.delete(0,END)
              self.txtDob.insert(END,sd[3])
              self.txtAge.delete(0,END)
              self.txtAge.insert(END,sd[4])
              self.txtGender.delete(0,END)
              self.txtGender.insert(END,sd[5])
              self.txtAdress.delete(0,END)
              self.txtAdress.insert(END,sd[6])
              self.txtMobile.delete(0,END)  
              self.txtMobile.insert(END,sd[7])
              self.txtMarks.delete(0,END)  
              self.txtMarks.insert(END,record[8])                         
       def DeleteData():
              
              if(len(stdId.get())!=0):
              		
              		pb.deleteRec(record[0])
              		clearData()
              		DisplayData()
       def searchDatabase():
              studentlist.delete(0,END)
              for item in tree.get_children():
              	tree.delete(item)
              
              S=[stdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Adress.get(),Mobile.get()]
              rows=pb.searchData(stdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Adress.get(),Mobile.get())
              for row in rows:
              		#print(row)
              		#studentlist.insert(END,row,str(""))
              		tree.insert('', END, values=row)
              if len(rows)==0:
              	showinfo(title='Information', message='No Information releated with  '+','.join(S))
                          
       def update():
              
              if(len(stdId.get())!=0):
                     pb.dataUpdate(stdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Adress.get(),Mobile.get(),Marks.get())
                     studentlist.delete(0,END)
                     studentlist.insert(END,(stdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Adress.get(),Mobile.get(),Marks.get()))
                     clearData()
                     DisplayData()
       def imports():
       	mydata.clear()
       	fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")))
       	with open(fln,'r') as myfile:
       		csvread=csv.reader(myfile,delimiter=",")
       		for i in csvread:
       			mydata.append(i)
       	updatecsv(mydata)
	
       def updatecsv(fl):
       	old=[]
       	for f in fl[1:]:
       		#studentlist.insert(END,(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7]))
       		a=pb.searchData(f[0],"","","","","","","")
       		if len(a)==0:
       			pb.addStdRec(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8])
       		else:
       			old.append(f[0])
       	showinfo(title='Information', message='StdID '+','.join(old)+' already exist')
       		
		
       def exports():
       	fname = filedialog.asksaveasfilename(filetypes=(("Txt files", "*.txt"), ("All files", "*.*")))
       	rows=[]
       	with open('project.txt') as f:
       		lines = f.readlines()
       		for line in lines:
       			rows.append(line)
       	with open(fname,'w') as f:
       		f.writelines(rows)
       	showinfo(title='Information', message='File Saved')
       	  

       #####################################FRAMES###################################################################
       MainFrame=Frame(self.root,bg="white")
       MainFrame.grid()  #THIS IS MAIN FRAME OUR WINDOW
       TitFrame=Frame(MainFrame,bd=1,padx=54,pady=8,bg="#FA603A",relief=RIDGE)
       TitFrame.pack(side=TOP)#THIS IS STITLE FRAME
       
       
    
       self.lblTit=Label(TitFrame,font=("Arial Bold", 50),text="Students Database Management System",bg="#FA603A",fg="black")
       self.lblTit.grid()

       self.lblTit=Label(TitFrame,font=('arial',25,'bold'),text="Indian Institute of Technology Mandi",bg="#FA603A",fg="black")
       self.lblTit.grid()

       self.lblTit=Label(TitFrame,font=('arial',12),text="(Priyanka)",bg="#FA603A",fg="black")
       self.lblTit.grid()

       ButtonFrame=Frame(MainFrame,bd=1,width=1390,height=70,padx=18,pady=10,bg="#FA603A",relief=RIDGE)
       ButtonFrame.pack(side=BOTTOM)#

       DataFrame=Frame(MainFrame,bd=19,width=1300,height=400,padx=10,pady=20,bg="#555",relief=RIDGE)
       DataFrame.pack(side=BOTTOM)#THIS IS STI
         
       DataFrameLeft=LabelFrame(DataFrame,font=('arial',12,'bold'),bd=1,width=450,height=400,bg="Ghost White",relief=RIDGE,text="STUDENT INFO\n")
       DataFrameLeft.pack(side=LEFT)
       DataFrameMid=LabelFrame(DataFrame,bd=0,width=10,height=250,bg="#555",relief=RIDGE)
       DataFrameMid.pack(side=LEFT)

       DataFrameRight=LabelFrame(DataFrame,font=('arial',12,'bold'),bd=1,width=500,height=400,bg="Ghost White",relief=RIDGE,text="STUDENT DETAILS\n")
       DataFrameRight.pack(side=RIGHT)
#########################################################Lables and entry widget #######################################################################
       #if(config['view'][0]=='yes'):
       	#print(config['view'][0])
       self.lblStdId=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Student Id:",bg="ghost white")
       self.lblStdId.grid(row=0,column=0,sticky=W)
       
       self.txtStdId=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=stdId,bg="ghost white",width=10)
       self.txtStdId.grid(row=0,column=1)#student id
       if(viewValue[0].lower()=='yes'):
	       self.lblFirstname=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="First Name:",bg="ghost white")
	       self.lblFirstname.grid(row=1,column=0,sticky=W)
	       self.txtFirstname=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Firstname,bg="ghost white",width=10)
	       self.txtFirstname.grid(row=1,column=1)#firstname


       if(viewValue[1].lower()=='yes'):
	       self.lblSurname=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Surname:",bg="ghost white")
	       self.lblSurname.grid(row=2,column=0,sticky=W)
	       self.txtSurname=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Surname,bg="ghost white",width=10)
	       self.txtSurname.grid(row=2,column=1)#surname

       if(viewValue[2].lower()=='yes'):
	       self.lblDob=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="DOB (DD/MM/YYYY)",bg="ghost white")
	       self.lblDob.grid(row=3,column=0,sticky=W)
	       self.txtDob=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=DoB,bg="ghost white",width=10)
	       self.txtDob.grid(row=3,column=1)#dateof birth

       if(viewValue[3].lower()=='yes'):
	       self.lblAge=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Age:",bg="ghost white")
	       self.lblAge.grid(row=4,column=0,sticky=W)
	       self.txtAge=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Age,bg="ghost white",width=10)
	       self.txtAge.grid(row=4,column=1)#age

       if(viewValue[4].lower()=='yes'):
	       self.lblGender=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Gender:",bg="ghost white")
	       self.lblGender.grid(row=5,column=0,sticky=W)
	       
	       self.txtGender=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Gender,bg="ghost white",width=10)
	       self.txtGender.grid(row=5,column=1)#gender

       if(viewValue[5].lower()=='yes'):
	       self.lblAdress=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Address:",bg="ghost white")
	       self.lblAdress.grid(row=6,column=0,sticky=W)
	       
	       self.txtAdress=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Adress,bg="ghost white",width=10)
	       self.txtAdress.grid(row=6,column=1)#adress

       if(viewValue[6].lower()=='yes'):
	       self.lblMobile=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Mobile:",bg="ghost white")
	       self.lblMobile.grid(row=7,column=0,sticky=W)
	       
	       self.txtMobile=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Mobile,bg="ghost white",width=10)
	       self.txtMobile.grid(row=7,column=1)#mobile
       if(viewValue[7].lower()=='yes'):
	       self.lblMarks=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Marks:",bg="ghost white")
	       self.lblMarks.grid(row=8,column=0,sticky=W)
	       
	       self.txtMarks=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Marks,bg="ghost white",width=10)
	       self.txtMarks.grid(row=8,column=1)#mobile

       ###############################List Box and ScrollBar Widget############################################
       scrollbar=Scrollbar(DataFrameRight)
       scrollbar.grid(row=0 ,column=0,sticky=tk.W)#scroll bar
      
       


       studentlist=Listbox(DataFrameRight,width=100,height=20,font=('arial',12,'bold'), yscrollcommand=scrollbar.set)
       
       #studentlist.bind('<<ListboxSelect>>',StudentRec)
       #studentlist.grid(row=0,column=0,padx=10)
       #scrollbar.config(command= studentlist.yview)
       cl=['StdID']
       if(viewValue[0].lower()=='yes'):
       	cl.append('Firstname')
       if(viewValue[1].lower()=='yes'):
       	cl.append('Surname')
       if(viewValue[2].lower()=='yes'):
       	cl.append('DoB')
       if(viewValue[3].lower()=='yes'):
       	cl.append('Age')
       if(viewValue[4].lower()=='yes'):
       	cl.append('Gender')
       if(viewValue[5].lower()=='yes'):
       	cl.append('Address')
       if(viewValue[6].lower()=='yes'):
       	cl.append('Mobile')
       if(viewValue[7].lower()=='yes'):
       	cl.append('Marks')	
       
       columns = (cl)
       tree = ttk.Treeview(DataFrameRight, columns=columns, show='headings')
       tree.column('StdID', width=100,anchor=tk.W)
       tree.heading('StdID', text='StdID')
       if(viewValue[0].lower()=='yes'):
       	tree.column('Firstname', width=150,anchor=tk.W)
       	tree.heading('Firstname', text='First Name')
       if(viewValue[1].lower()=='yes'):
       	tree.column('Surname', width=150,anchor=tk.W)
       	tree.heading('Surname', text='Last Name')
       if(viewValue[2].lower()=='yes'):
       	tree.column('DoB', width=100,anchor=tk.CENTER)
       	tree.heading('DoB', text='DoB')
       if(viewValue[3].lower()=='yes'):
       	tree.column('Age', width=30,anchor=tk.CENTER)
       	tree.heading('Age', text='Age')
       if(viewValue[4].lower()=='yes'):
       	tree.column('Gender', width=60,anchor=tk.W)
       	tree.heading('Gender', text='Gender')
       if(viewValue[5].lower()=='yes'):
       	tree.column('Address', width=100,anchor=tk.CENTER)
       	tree.heading('Address', text='Address')
       if(viewValue[6].lower()=='yes'):
       	tree.column('Mobile', width=70,anchor=tk.W)
       	tree.heading('Mobile', text='Mobile')
       if(viewValue[7].lower()=='yes'):
       	tree.column('Marks', width=60,anchor=tk.CENTER)
       	tree.heading('Marks', text='Marks')
       

       tree.bind('<<TreeviewSelect>>', item_selected)
       tree.grid(row=0, column=1, padx=10,sticky=tk.E)

       #######################################Button Widget####################################################
       self.btnAddData=Button(ButtonFrame,text="Add New",font=('arial',10,'bold'),height=1,width=8,bd=3,fg="#555",command=addData)
       self.btnAddData.grid(row=0,column=0)#ADD NEW

       self.btnDisplay=Button(ButtonFrame,text="Display",font=('arial',10,'bold'),height=1,width=8,bd=3,fg="#555",command=DisplayData)
       self.btnDisplay.grid(row=0,column=1)#DISPLAY

       self.btnClear=Button(ButtonFrame,text="Clear",font=('arial',10,'bold'),height=1,width=8,bd=3,fg="#555",command=clearData)
       self.btnClear.grid(row=0,column=2)#CLEAR

       self.btnDelete=Button(ButtonFrame,text="Delete",font=('arial',10,'bold'),height=1,width=8,bd=3,fg="#555",command=DeleteData)
       self.btnDelete.grid(row=0,column=3)#DELETE

       self.btnSearch=Button(ButtonFrame,text="Search",font=('arial',10,'bold'),height=1,width=8,bd=3,fg="#555",command=searchDatabase)
       self.btnSearch.grid(row=0,column=4)#SEARCH

       self.btnUpdate=Button(ButtonFrame,text="Update",font=('arial',10,'bold'),height=1,width=8,bd=3,fg="#555",command=update)
       self.btnUpdate.grid(row=0,column=5)#UPDATE
       
       self.btnUpdate=Button(ButtonFrame,text="Import",font=('arial',10,'bold'),height=1,width=8,bd=3,fg="#555",command=imports)
       self.btnUpdate.grid(row=0,column=6)#IMPORT
       
       self.btnUpdate=Button(ButtonFrame,text="Export",font=('arial',10,'bold'),height=1,width=8,bd=3,fg="#555",command=exports)
       self.btnUpdate.grid(row=0,column=7)#EXPORT

       self.btnExit=Button(ButtonFrame,text="Exit",font=('arial',10,'bold'),height=1,width=8,bd=3,fg="#555",command=iExit)
       self.btnExit.grid(row=0,column=8)#EXIT

if __name__=='__main__':
   root=Tk()#CREATE AN OBJECT
   application=Student(root)#PASS IT TO OUR CLASS WHITH ITS PROPERTIES IN CLASS
   root.mainloop()#RUN UNTIL CLOSING THE WINDOW MANUALLY
