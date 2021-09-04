
#calculator

# def add(a,b):
#     return a+b
#     #print(a,"+",b,"=",c)
# def sub(a,b):
#     return a-b
#     #print(a,"-",b,"=",c)
# def mul(a,b):
#     return a*b
#     #print(a,"*",b,"=",c)
# def div(a,b):
#     return a/b
#     #print(a,"/",b,"=",c)
#
# print("1.Addition"
#       "2.Subtraction"
#       "3.Multiplication"
#       "4.Division"
#       "Enter option")
# while True:
#     d=int(input("Enter option"))
#     a=float(input("Enter no 1"))
#     b=float(input("Enter no 2"))
#     if d==1:
#         print(add(a,b))
#     elif d==2:
#         print(sub(a,b))
#     elif d==3:
#         print(mul(a,b))
#     elif d==4:
#         print(div(a,b))
#     else:
#         print("Enter correct option")

#fibonacci

# i1=int(input("Enter no "))
#
# n1=0
# n2=1
# for i in range(i1):
#     print(n1)
#     n3=n1+n2
#     n1=n2
#     n2=n3

#011235813

#prime

# a=int(input("Enter a no"))
# flag=0
# if a>1:
#  for i in range(2,a):
#     if a%i==0:
#         break
#  else:
#         flag=1
# if flag==1:
#     print("prime")
# else:
#     print("not prime")


#rangeprime

# a=int(input("Enter no"))
# b=int(input("Enter no"))
#
# flag=0
# for j in range(a,b+1):
#  for i in range(2,j):
#     if j%i==0:
#         break
#  else:
#     print(j)

#palindrome
# a="abc"
# b=a[::-1]
# print(b)

a=input("Enter string")
b=a[::-1]
if b==a:
    print("Palindrome")
else:
    print(" not Palindrome")

