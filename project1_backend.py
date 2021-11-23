
#import project1_frontend
import csv
import os

def studentData():
	return 1
                 
def addStdRec(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile,Marks):
	if len(Mobile)==0:
		Mobile='0';
	if len(Firstname)==0:
		Firstname='NA';
	if len(Surname)==0:
		Surname='NA';
	if len(DoB)==0:
		DoB='0';
	if len(Age)==0:
		Age='0';
	if len(Gender)==0:
		Gender='NA';
	if len(Address)==0:
		Address='NA';
	if len(Mobile)==0:
		Mobile='NA';
	if len(Marks)==0:
		Marks='0';
	S=[StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile, Marks]
	lock=1
	
	with open('project.txt') as f:
		lines = f.readlines()
		for line in lines:
			ln=line.split(",")
			if (ln[0]==StdID):
				lock=0
				
				
	#print("lock ",lock)
	if lock!=0:			
		with open('project.txt','a+') as f:
			f.write(",".join(S)+'\n')
	return lock
        
def viewData():
	row=[]
	with open('project.txt') as f:
		lines = f.readlines()
		for line in lines:
			row.append(line.split(","))
			#print(row)
	return row
def deleteRec(StdID):
	rows=[]
	
	StdID=str(StdID)
	with open('project.txt') as f:
		lines = f.readlines()
		for line in lines:
			ln=line.split(",")
			
			if (ln[0]==StdID):
				pass
			else:
				
				rows.append(line)
	with open('project.txt','w') as f:
			f.writelines(rows)
			
                
def searchData(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile):
	#print(StdID)
	row=[]
	with open('project.txt') as f:
		lines = f.readlines()
		for line in lines:
			ln=line.split(",")
			
			if (ln[0]==StdID or ln[1].lower()==Firstname.lower() or ln[2].lower()==Surname.lower() or ln[3]==DoB or ln[4]==Age or ln[5].lower()==Gender.lower() or ln[6].lower() ==Address.lower() or ln[7] ==Mobile):
				
				row.append(ln)
	return row
def dataUpdate(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile,Marks):
	row=[]
	with open('project.txt') as f:
		lines = f.readlines()
		for line in lines:
			ln=line.split(",")
			
			if (ln[0]==StdID):

				row.append(ln)
	
	#print(row)
	if len(Firstname)==0:
		Firstname=row[0][1];
	if len(Surname)==0:
		Surname=row[0][2];
	if len(DoB)==0:
		DoB=row[0][3];
	if len(Age)==0:
		Age=row[0][4];
	if len(Gender)==0:
		Gender=row[0][5];
	if len(Address)==0:
		Address=row[0][6];
	if len(Mobile)==0:
		Mobile=row[0][7];
	if len(Marks)==0:
		Marks=row[0][8];
	deleteRec(StdID)
	addStdRec(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile,Marks)
           
