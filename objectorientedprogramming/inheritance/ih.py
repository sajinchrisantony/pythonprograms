#single inheritence

# class Person: #base class/parent class/super class
#     def walk(self):
#         print("person is walking")
#     def read(self):
#         print("person is reading")
#
# class Student(Person): #derived class/sub class/child class
#     def exam(self):
#         print("student attending exam")
#
# pe=Person()
# pe.walk()
# pe.read()
# st=Student()
# st.exam()
# st.walk()
# st.read()

#person employee class

# class Person:
#     def details(self,name,age):
#         self.name=name
#         self.age=age
#     def print(self):
#         print(self.name)
#         print(self.age)
#
# class Employee(Person):
#     def details1(self, eid, salary):
#             self.eid = eid
#             self.salary = salary
#
#     def print1(self):
#             print(self.eid)
#             print(self.salary)
#
#
#
# p2=Employee()
# p2.details("sajin",23)
# p2.details1(1,24000)

# p2.print1()

# p2.print()


#person...child
#multiple inheritence
# class Person:
#      def set(self,name,age):
#          self.name=name
#          self.age=age
#          print(self.name,self.age)
# class Child:
#     def setv(self,school,std):
#         self.school=school
#         self.std=std
#         print(self.school,self.std)
# class Student(Person,Child):
#     def printv(self,rollno,mark):
#         self.rollno=rollno
#         self.mark=mark
#         print(self.rollno,self.mark)
#
# st=Student()
# st.set("sajin",23)
# st.setv("dnc",12)
# st.printv(1,100)

#student...parent ...person,child


#person parent employee
# class Employee:
#     def set1(self, eid, salary):
#         self.eid = eid
#         self.salary = salary
#         print(self.eid,self.salary)
# class Person(Employee):
#     def set(self, name, age):
#         self.name = name
#         self.age = age
#         print(self.name, self.age)
#
# class Parent(Employee):
#     def set2(self, pname):
#         self.pname = pname
#         print(self.pname)
#
#
# obj=Person()
# obj.set("sajin",23)
# obj.set1(1,25000)
#
# obj=Parent()
# obj.set2("nijas")
# obj.set1(2,26000)
#


#person parent teacher

#multilevel inheritence/hierarchical inheritance

# class A:
#     def printA(self):
#         print("inside A")
#
# class B(A):
#     def printB(self):
#         print("inside B")
#
# class C(B):
#     def printC(self):
#         print("inside C")
#
# a=A()
# a.printA()
#
# b=B()
# b.printB()
# b.printA()
#
# c=C()
# c.printC()
# c.printB()
# c.printA()


#person child student

# class Person:
#     def det(self,pname):
#         self.pname=pname
#         print(self.pname)
#
# class Child(Person):
#     def det1(self,cadd):
#         self.cadd=cadd
#         print(self.cadd)
#
# class Student(Child):
#     def det2(self,sid):
#         self.sid=sid
#         print(self.sid)

# s1=Student()
# s1.det2(5)
# s1.det1("thoppumpady")
# s1.det("sajin")



#person child parent student
#child parent inherits...person
#student class  inherits...child

# class Person:
#     def det(self,pname):
#         self.pname=pname
#         print(self.pname)
#
# class Child(Person):
#     def det1(self,cadd):
#         self.cadd=cadd
#         print(self.cadd)
#
# class Student(Child):
#     def det2(self,sid):
#         self.sid=sid
#         print(self.sid)
#
# class Parent(Person):
#     def det3(self,pno):
#         self.pno=pno
#         print(self.pno)
#
# s1=Student()
# s1.det2(1)
# s1.det1("thoppumpady")
# s1.det("sajin")
#
# p1=Parent()
# p1.det3("9446879523")
# p1.det("antony")

#constructor and inheritence
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printVal(self):
#         print("name",self.name)
#         print("age",self.age)
# class Student(Person):
#     def __init__(self,rollno,mark,name,age):
#         super().__init__(name,age)
#         self.rollno=rollno
#         self.mark=mark
#     def print(self):
#         print(self.rollno)
#         print(self.mark)
# cr=Student(2,55,"Sajin",23)
# cr.printVal()
# cr.print()
#
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printVal(self):
#         print("name",self.name)
#         print("age",self.age)
# class Employee(Person):
#     def __init__(self,job,salary,name,age):
#         super().__init__(name,age)
#         self.job=job
#         self.salary=salary
#     def print(self):
#         print(self.job)
#         print(self.salary)\
#
# emp=Employee("ceo",55000,"Sajin",23)
# emp.printVal()
# emp.print()

#2 string method
#to return our string instead of reference ipaddress

class Vehicle:
    def __init__(self,model,regno,color):
        self.model=model
        self.regno=regno
        self.color=color

    def printv(self):
        print(self.model,self.color,self.regno)

    def __str__(self):
        return self.model+self.color
ve=Vehicle("KTM","kl34b3343","WHITE")
ve.printv()

print(ve)

# class Student:
#     def __init__(self,nm,rn,dp,co):
#         self.nm=nm
#         self.rn=rn
#         self.dp=dp
#         self.co=co
#
#     def printv(self):
#         print(self.nm,self.rn,self.dp,self.co)
#
#     def __str__(self):
#         return self.nm+str(self.rn)
# s1=Student("sajin",1,"IT","RSET")
# s1.printv()
#
# print(s1)

#parent teacher constr. inhert. str name ,id
# class Parent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printVal(self):
#         print("name",self.name)
#         print("age",self.age)
# class Teacher(Parent):
#     def __init__(self,id,dp,name,age):
#         super().__init__(name,age)
#         self.id=id
#         self.dp=dp
#     def print(self):
#         print(self.id)
#         print(self.dp)
#     def __str__(self):
#         return self.name+" "+str(self.id)
#
#
# t1=Teacher(1,"CS","Sajin",23)
# t1.printVal()
# t1.print()
#
# print(t1)

#polymorphism
#overriding ..same method name and same no of arguments
#overloading ..same method name and diff no of parameters

#overloading

# class Person:
#     def show(self,num1):
#         self.num1=num1
#         print(self.num1)
# class Student(Person):
#     def show(self,num2,num3):
#         self.num2=num2
#         self.num3=num3
#         print(self.num2,self.num3)
#
# per=Student()
# per.show(1)

# class teacher:
#     def show(self,nm):
#         self.nm=nm
#         print(self.num1)
# class Student(teacher):
#     def show(self,nm1,nm2):
#         self.nm1=nm1
#         self.nm2=nm2
#         print(self.nm1+self.nm2)
#
# per=Student()
# per.show(1)

#overriding

# class Person:
#     def printval(self,nm):
#         self.nm=nm
#         print(self.nm)
#
# class Child(Person):
#     def printval(self,class1):
#         self.class1=class1
#         print("Inside child method",self.class1)
#
# ch=Child()
# ch.printval("abc")#child class method overrides person class method

# class Person:
#     def val(self,nm):
#         self.nm=nm
#         print(self.nm)
#
# class Child(Person):
#     def val(self,nm1):
#         self.nm1=nm1
#         print("inside child",self.nm1)
#
# ch=Child()
# ch.val("1")


