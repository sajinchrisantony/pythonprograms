# a=int(input("Enter 1st"))
# b=int(input("Enter 2nd"))
# c=a/b
# print(c)
# zero error possible

# a=int(input("Enter 1st"))
# b=int(input("Enter 2nd"))
#
# try:
#  c=a/b
#  print(c)
#
# except:
#  print("Exception Occured")

# lst=[1,2,3]
# #print(lst[4]) error
# a=int(input("Enter index"))
#
# try:
#     print(lst[a])
# except:
#     print("NO INDEX in lst")

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

# lst=[1,2,3,4]
# pos=int(input("Enter index"))
# try:
#  print(lst[pos])
# except Exception as e:
#     print(e.args)

#Exception div by 0
# a=int(input("Enter 1"))
# b=int(input("Enter 2"))
#
# try:
#
#  print(a/b)
# except Exception as e:
#     print(e.args)

#raising our own exceptions as error

# a=int(input("Enter 1"))
# b=int(input("Enter 2"))
#
# if b>a:
#     raise Exception ("No 2 is greater")
# else:
#  print(a/b)

 #18 above vaccine check

a=int(input("Enter your age"))

if a<18:
    raise Exception ("You are not eligible for vaccine")
else:
    print("You are eligible for vaccine")


try and finally block works everytime but Exception works only when there is exceptions