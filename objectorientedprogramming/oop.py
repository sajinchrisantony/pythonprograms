# oop
#class ... design pattern
#object...real world entity
#reference...operations

#class
# class Person:
#     def walk(self): #instance keyword
#         print("Person is walking")
#     def read(self):
#         print("person is reading")
#
# #object
# pe1=Person()
# pe1.walk()
# pe1.read()
#
# #object2
# pe2=Person()
# pe2.walk()
# pe2.read()


# class book:
#     def paper(self):
#         print("book contain paper")
#     def cover(self):
#         print("book contain cover")
#
#
# b1=book()
# b1.paper()
# b1.cover()
#
#
# a=book()
# a.paper()
# a.cover()


# class Person:
#     def setvalue(self,name,age):
#         self.name=name
#         self.age=age
#     def printvalue(self):
#         print("Name",self.name)
#         print("Age",self.age)
#
# pe=Person()
# pe.setvalue("Sajin",23)
# pe.printvalue()

#id,name,salary,age,company name,department

# class employee:
#     def setvalue(self,id,name,age,salary,cname,dname):
#         self.id1 = id
#         self.name1 = name
#         self.age1 = age
#         self.salary1 = salary
#         self.cname1 = cname
#         self.dname1 = dname
#     def printvalue(self):
#         print("ID",self.id1,"Name",self.name1)
#         print("Age", self.age1)
#         print("Salary", self.salary1)
#         print("Company Name", self.cname1)
#         print("Department Name", self.dname1)
#
#
# e1=employee()
# e1.setvalue(1,"Sajin",23,25000,"Microsoft","IT")
# e1.printvalue()
# print("\n")
# e2=employee()
# e2.setvalue(2,"NIjas",32,50000,"Dell","Marketing")
# e2.printvalue()

#Addition program

# class Addition:
#     def set(self,n1,n2):
#         self.no1=n1
#         self.no2=n2
#         print("Sum=",self.no1+self.no2)
#
# pe=Addition()
# num1=int(input("Enter1"))
# num2=int(input("Enter2"))
#
# pe.set(num1,num2)


# class Student:
#
#     def setvalue(self,rno,name,cls,sch):
#         self.rno=rno
#         self.name=name
#         self.cls=cls
#         self.sch=sch
#
#     def print(self):
#         print(self.rno,self.name,self.cls,self.sch)
#
# s1=Student()
# s1.setvalue(1,"sajin",12,"KV")
# s1.print()

#types of variables
#1.instance variable...related to methods..access using self
#2.static variable...related to class...access using class name
# class Student:
#     sch="KV" #static variable
#     def setvalue(self,rno,name,cls):
#         self.rno=rno
#         self.name=name
#         self.cls=cls
#
#     def print(self):
#         print(self.rno,self.name,self.cls,Student.sch)
#
# s1=Student()
# s1.setvalue(1,"sajin",12)
# s1.print()
#


# class Employee:
#     cname="Microsoft"
#     def setvalue(self,id,name,age,salary,dname):
#         self.id1 = id
#         self.name1 = name
#         self.age1 = age
#         self.salary1 = salary
#         self.dname1 = dname
#     def printvalue(self):
#         print("ID",self.id1,"Name",self.name1)
#         print("Age", self.age1)
#         print("Salary", self.salary1)
#         print("Company Name", Employee.cname)
#         print("Department Name", self.dname1)
#
#
# e1=Employee()
# e1.setvalue(1,"Sajin",23,25000,"IT")
# e1.printvalue()
# print("\n")
# e2=Employee()
# e2.setvalue(2,"NIjas",32,50000,"Marketing")
# e2.printvalue()

#account creation depost withdrawal

# class Bank:
#
#     def ac(self,no,name,balance):
#         self.no=no
#         self.name=name
#         self.balance=balance
#     def deposit(self,damt):
#          self.damt=damt
#          self.balance+=self.damt
#     def withdrawal(self,wamt):
#           self.wamt=wamt
#           self.balance-=self.wamt
#     def print(self):
#         print(self.no,self.name,self.balance)
# b1=Bank()
# b1.ac(1,"sajin",5000)
# b1.print()
# b1.deposit(5000)
# b1.print()
# b1.withdrawal(2000)
# b1.print()

#madam
# class Bank:
#     bname="SBI"
#     def acCreate(self,acno,name):
#         self.acno=acno
#         self.name=name
#         self.minimumbal=5000
#         self.balance=self.minimumbal
#     def deposit(self,amt):
#         self.amt=amt
#         self.balance+=self.amt
#         print(Bank.bname,"account credited with amt",self.amt)
#         print("Balance=",self.balance)
#
#     def withdrw(self,amnt):
#         self.amnt=amnt
#         if self.amnt>self.balance:
#             print("Insufficient Balance")
#         else:
#             print("Account debited with",self.amnt)
#             self.balance-=self.amnt
#             print("Balance",self.balance)
#
# obj=Bank()
# num=int(input("Enter ac num"))
# obj.acCreate(num,"Sajin")
# obj.deposit(5000)
# obj.withdrw(2000)

#constructors used to initialize instance variables
# __init__ .....constructor
# class Person:
#     def __init__(self,name,age,address):#constructor
#         self.name=name
#         self.age=age
#         self.address=address
#     def printval(self):
#         print(self.name,self.age,self.address)
#
# obj=Person("Anu",34,"abc")
# obj.printval()

#employee class with constructor

# class Employee:
#     cname="Microsoft"
#     def __init__(self,id,name,age,salary,dname):
#         self.id1 = id
#         self.name1 = name
#         self.age1 = age
#         self.salary1 = salary
#         self.dname1 = dname
#     def printvalue(self):
#         print("ID",self.id1,"Name",self.name1)
#         print("Age", self.age1)
#         print("Salary", self.salary1)
#         print("Company Name", Employee.cname)
#         print("Department Name", self.dname1)
#
#
# e1=Employee(1,"Sajin",23,25000,"IT")
# e1.printvalue()

#calculator with constructors

# class Calc:
#
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#     def add(self):
#         return self.a+self.b
#
#     def sub(self):
#         return self.a-self.b
#
#     def mul(self):
#         return self.a*self.b
#
#     def div(self):
#         return self.a/self.b
#
# a=int(input("Enter no1"))
# b=int(input("Enter no2"))
# obj=Calc(a,b)
# print(obj.add())
# print(obj.sub())
# print(obj.mul())
# print(obj.div())


#Teacher tname,subject,department,tid,college name .. create with constructor and static variable

class Teacher:
    cn="Rajagiri"
    def __init__(self,tname,sub,depart,tid):
        self.tname=tname
        self.sub=sub
        self.depart=depart
        self.tid=tid
    def print(self):
        print(self.tname,self.sub,self.depart,self.tid,Teacher.cn)

obj=Teacher("Sajin","Maths","MC",1)
obj.print()
