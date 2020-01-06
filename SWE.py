#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os

class person:
    name=''
    id=0
    gender=''
    
    
    def __init__(self):
        name=''
        id=0
        gender=''
        pass
    
    
    def getname(self):
        return self.name
    
    
    def getid(self):
        return self.id
    
    
    def getgender(self):
        return self.gender
    
    
    def setname(self,a):
        self.name=a
    
    
    def setid(self,a):
        self.id=a
    
    
    def setgender(self,a):
        self.gender=a
        
    
class teacher(person):
    designation=''
    pay=0
    
    
    def getpay(self):
        return pay
    
    
    def setpay(self,a):
        self.pay=a
    
    
    def __init__(self):
        designation=''
        shift=''
    
    
    def getdesignation(self):
        return self.designation
    
    
    def setdesignation(self,a):
        self.designation=a
        
        
     
    def setid(self, a):
        id=a
    def setname(self,a):
        name=a
        

class student (person):
    rollno = 0
    department = ''
    
    
    def __init__(self):
        rollno = 0
        department = ''

        
    def getrollno(self):
        return self.rollno
    
    
    def getdepartment(self):
        return self.department
    
    
    def setrollno(self,a):
        self.rollno=a
       
    
    def setid(self, a):
        id=a
    def setname(self,a):
        name=a
    
    def setdepartment(self,a):
        self.department=a
        
        

class section:
    teacher_ = teacher()        
    students=[]
    no_of_students=0
    
    
    def __init__(self):
        pass

    def add_student(self):
        if self.no_of_students < 10 :
            a=str(input("Enter the name "))
            b=str(input("Enter the rollno "))
            c=str(input("Enter the department "))
            stu=student()
            stu.setrollno(b)
            stu.setdepartment(c)
            self.students.append(stu)
            file = open('Student.txt', "a")
            leng =len(self.students)
            
            aa="The name of the student is "+ a + '\n'
            bb="The rollno of the student is "+ b+ '\n'
            cc="The department of the student is "+ c+ '\n'
            file.write("Student no " + str(leng) +'\n')
            file.write(aa)
            file.write(bb)
            file.write(cc)
            file.write('\n')
            file.write('\n')
            file.close()
    
    def add_teacher(self):
        a=str(input("Enter the name "))
        b=str(input("Enter the designation "))
        c=str(input("Enter the ID "))
        teacher1=teacher()
        teacher1.setdesignation(b)
        teacher1.setid(c)
        teacher1.setname(a)
        self.teacher_=teacher1
        file = open('Teacher.txt', "a")
        #leng =len(self.teacher_)
        aa="The name of the Teacher is "+ a + '\n'
        bb="The designation of the teacher is "+ b+ '\n'
        cc="The id of the teacher is "+ c+ '\n'
        file.write("The teacher for this course is "  +'\n') 
        file.write(aa)
        file.write(bb)
        file.write(cc)
        file.write('\n')
        file.close()  
        
        
        
class class_():
    section=[]
    no=3
    name=''
    course_code=''
    def __init__(self):
        pass
    
    def addclass(self):
        a=str(input("Enter the name of the course "))
        b=str(input("Enter the course id  "))
        c=str(input("Enter the credit hours  "))
        file = open('Course.txt', "a")
        aa="The name of the course is "+ a + '\n'
        bb="The Course code is  "+ b+ '\n'
        cc="The Credit hours are  "+ c+ '\n'
        file.write(aa)
        file.write(bb)
        file.write(cc)
        file.write('\n')
        
        
        

class file_handling():
    def __init__():
        pass
    
    
    def create_file():
        file_name = str(input ("please enter the name of the file to be created "))
        file_name = file_name + '.txt'
        f = open(file_name,"w+")


    def remove_file():
        file_name = str(input("please enter the name of the file to be deleted "))
        file_name = file_name + '.txt'
        if os.path.isfile('./' + file_name):
            os.remove(file_name)
            print("File Removed!")
        else:
            print ('file does not exist')


    def show_file():
        file_name = str(input("please enter the name of the file to be shown "))
        file_name = file_name + '.txt' 
        if os.path.isfile('./' + file_name):
            file = open(file_name, "r")
            for line in file:
                print(line)
        else:
            print('file not found ')


    def update_file():
        file_name = str(input("please enter the name of the file to be updated "))
        file_name = file_name + '.txt'
        choice = str(input ("please enter 'a' for append and 'o' for overwrite "))
        if choice =='a':
            msg = ''
            if os.path.isfile('./' + file_name):
                file = open(file_name, "a")
                while True:
                    msg = str(input ("please enter the line of message to be updated to the file or 'e' to end the writing "))
                    if msg != 'e':
                        msg="\n" + msg
                        file.write(msg)
                    else: 
                        break
                file.close()
            else:
                print ('file does not exist')
        if choice =='o':
            if os.path.isfile('./' + file_name):
                file = open(file_name, "w")
                while True:
                    msg = str(input ("please enter the line of message to be updated to the file or 'e' to end the writing "))
                    if msg != 'e':
                        file.write(msg + "\n")
                    else:
                        break
                file.close()
            else:
                print ('file does not exist')


    def find_in_file():
        file_name = str(input("please enter the name of the file to do the search in "))
        file_name = file_name + '.txt'
        if os.path.isfile('./' + file_name):
            input_ = str(input("please enter the string you want to find "))
            file = open(file_name, "r")
            for i, line in enumerate(file,1):
                num=line.find(input_)
                if num==0:
                    print('string found on line number ' + str(i))
        else:
            print ('File not found ')

    def replace_in_file():
        file_name = str(input("please enter the name of the file to do the replacing  "))
        file_name = file_name + '.txt'
        if os.path.isfile('./' + file_name):
            input_ = str(input("please enter the string you want to replace "))
            input1_ = str(input("please enter the string you want to replace with "))
            file = open(file_name,"r")
            i=0
            file_dump=''
            for line in file:
                file_dump += line.replace(input_,
                                          input1_)
            file = open(file_name, "w")
            file.write(file_dump)
            file.close()
        else:
            print ('file not found')
            
            
            


# In[ ]:




