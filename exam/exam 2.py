#1

# class vehicle:
#     type1="private"
#     type2='0001'
#     def details(self,no,color,mvd):
#         self.no=no
#         self.color=color
#         self.mvd=mvd
#
#     def printdet(self):
#         print(self.no)
#         print(self.color)
#         print(self.mvd)
#
#
# class bus(vehicle):
#     def bdet(self,bstart,bend):
#         self.bstart=bstart
#         self.bend=bend
#
#     def printbdet(self):
#         print(self.bstart)
#         print(self.bend)
#         print(self.type1)
#
# b1=bus()
# b1.details("KL23b1234","green","Ernakulam")
# b1.printdet()
# b1.bdet("Trivandrum","Kochi")
# b1.printbdet()
# #print(b1.type1)
# print(b1.type2)

#2

# class Person:
#     def det(self,pname):
#         self.pname=pname
#         print(self.pname)
#
# class Child(Person):
#     def det1(self,caddress):
#         self.caddress=caddress
#         print(self.caddress)
#
# class Parent(Person):
#     def det2(self,pno):
#         self.pno=pno
#         print(self.pno)
#
# class Student(Child,Parent):
#     def det3(self,sid):
#         self.sid=sid
#         print(self.sid)
#
# s1=Student()
# s1.det("Sajin")
# s1.det1("kochi")
# s1.det2("9991234657")
# s1.det3("23")
#


#3


class book:
    lname = "ekm"
    def __init__(self,bname,author,pages):
        self.bname=bname
        self.author=author
        self.pages=pages

    def printdet(self):
        print(book.lname)
        print(self.bname)
        print(self.author)
        print(self.pages)

b1=book("Adventures","Thomas","455")
b1.printdet()

#4



# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printVal(self):
#         print("name",self.name)
#         print("age",self.age)
# class Dog(Animal):
#     def __init__(self,wt,name,age):
#         super().__init__(name,age)
#         self.wt=wt
#     def print(self):
#         print("weight",self.wt)
#
#
# d1=Dog(5,"Dobber",23)
# d1.printVal()
# d1.print()


#5.
# Same method name and same number of arguments.
# child class overrides parent class method

# class book:
#     def val(self,nm):
#         self.nm=nm
#         print(self.nm)
#
# class magazine(book):
#     def val(self,nm1):
#         self.nm1=nm1
#         print("inside child magazine",self.nm1)
#
# b1=magazine()
# b1.val("1")


#6.
#
# class Student:
#     def __init__(self,nm,id,dp,mk):
#         self.nm=nm
#         self.id=id
#         self.dp=dp
#         self.mk=mk
#
#     def printvalue(self):
#         print("name::",self.nm)
#         print("id::",self.id)
#         print("department::",self.dp)
#         print("mark::",self.mk)
#
#     def __str__(self):
#         return self.nm
#
# f1=open("exam2file",'r')
# for line in f1:
#     l=line.split(",")
#     name=l[0]
#     age=l[1]
#     dept=l[2]
#     mark=l[3]
#
#     st=Student(name,age,dept,mark)
#7.

# import re
# x='[+][9][1]\d{10}$'
# f1=open("exam2file2",'r')
# f2=open("validphone",'w')
# for i in f1:
#  number=i.rstrip("\n")
#  match=re.fullmatch(x,number)
#  if match!=None:
#     f2.write(number)

#8.
# finally block executes after try block
# it also gets executed if exception happens
# lst=[1,2,3]
# #print(lst[4]) error
# a=int(input("Enter index"))
#
# try:
#     print(lst[a])
# except:
#     print("NO INDEX in lst")
# finally:
#     print("Inside finally")

#9.

#
# import re
#
# n = input("Enter")
#
# x = '[^[A-Z]\W{5,10}*[A-Z]]'
# match = re.fullmatch(x, n)
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")



#10

# import re
# x="[A-Z][a-z]"
# matcher=re.finditer(x,'abBc5t Vc@c A68b Ab df a7')
# for match in matcher:
#     print("match available at",match.start())
#     print("group=",match.group())

#11

# import re
# n=input("Enter")
# x='^a[0-9]*b$'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")

#12

# class vehicle:
#     def __init__(self,model,regno):
#         self.model=model
#         self.regno=regno
#
#     def printv(self):
#         print(self.model,self.regno)
#
#     def __str__(self):
#         return self.regno
# v1=vehicle("KTM","kl34b3343")
# v1.printv()
#
# print(v1)

#13

# number = int(input("Enter a number"))
# even = lambda number: "Even Number" if number % 2 == 0 else "Odd Number"
#
# print(even(number))