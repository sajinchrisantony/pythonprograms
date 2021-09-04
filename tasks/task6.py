# a=int(input("Enter a number"))
#
# if a>0:
#
#   if a%2==0:
#     print("Even")
#   else:
#     print("Odd")
#
# else:
#     print("cannot, enter positive")
#


# a=int(input("Enter min"))
# b=int(input("Enter max"))
#
# for i in range (a,b+1):
#     if i%2==0:
#         print("even",i)


# a=int(input("Enter number"))
# sum=0
# for i in range (1,a+1):
#     if i%2==0:
#         sum+=i
# print(sum)

# a=int(input("Enter number"))
# sum=0
# i=1
# while i<=a:
#     sum+=i
#     i+=1
#
# print(sum)

# a=int(input("Enter number"))
# pr=1
# i=1
# while i<=a:
#     pr*=i
#     i+=1
# print(pr)

a=int(input("Enter number"))
if a>0:
 pr=1
 for i in range(1,a+1):
    pr*=i
 print(pr)
elif a==0:
 print("1")

else:
 print("Enter positive")

