#functions
# num1=int(input("Enter no1"))
# num2=int(input("Enter no2"))
# res=num1+num2
# print("result",res)

#function without arguments
# def add():
#     num1 = int(input("Enter no1"))
#     num2 = int(input("Enter no2"))
#     res = num1 + num2
#     print("result", res)
# add()
# add()

# function with arguments
# def add(num1,num2):
#  print(num1+num2)
# add(1,2)
# add(55,45)

#function with arguments and return types
# def add(num1,num2):
#     return num1+num2
# print(add(1,2))

#function without argument odd or even

# def check():
#     num=int(input("Enter a number"))
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# check()

#function with argument factorial of a number

# def fact(num):
#     if num>0:
#      pro=1
#      for i in range(1,num+1):
#          pro*=i
#      print(pro)
#
#     elif num==0:
#         print(1)
#     else:
#         print("Enter positive")
#
# fact(-3)



#factorial func with arguments and return type

# def factorial(fact):
#     s=1
#     if fact>0:
#         for i in range (1,fact+1):
#             s*=i
#         return s
#     elif fact==0:
#         return "factorial of 0 is 1"
#     else:
#         return "factorial does not exist for negative"
#
# print(factorial(-1))


#sum to n numbers

# def sum(num):
#     sum=0
#     for i in range(1,num+1):
#         sum+=i
#     return(sum)
# print(sum(5))
#
# def sum(n):
#     s=0
#     for i in range(1,n+1):
#         s+=i
#     print(s)
# sum(5)
#

# while True:
#     print("hello")
#
# while False:
#     print("hello")

x=5
def foo():
    global x
    x+=10
    print("local",x)
foo()
print("global",x)
