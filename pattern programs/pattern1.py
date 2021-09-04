# print("hello")
# print("\r")
# print("hai")
# 00
# 10 11
# 20 21 22
# 30 31 32 33
#        *
#        **
#        ***
#        ****

for i in range(5):
    for j in range(0,i):
        print("*",end=" " )
    print("\r")
#
# *****
# ****
# ***
# **
# *
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" " )
#     print("\r")

# 1
# 23
# 456

# def pat(n):
#  num=1
#  for i in range(n):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print("\r")
#
# pat(4)

# 1
# 12
# 123
# 1234
# def pat(n):
#  for i in range(n):
#     for j in range(1,i):
#         print(j,end=" ")
#
#     print("\r")
# pat(6)

# def pat(n):
#  num=1
#  for i in range(n):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#
#     print("\r")
# pat(5)

# *****
# *****
# *****
# *****
# def square(n):
#  for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()
# square(6)

    #    *
    #   * *
    #  * * *
    # * * * *

# k=6
# for i in range(6):
#     for r in range(k):
#         print(end=" ")
#     k=k-1
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

 # * * * * *
 #  * * * * *
 #   * * * * *
 #    * * * * *
 #     * * * * *
# k = 1
# for i in range(5):
#     for r in range(k):
#         print(end=" ")
#     k = k + 1
#     for j in range(0, 5):
#         print("*", end=" ")
#     print()

# def parallel(n):
#     k=n
#     for i in range(0,n):
#         for r in range(0,k):
#             print(end=" ")
#         k=k+1
#         for j in range(0,n):
#             print("* ",end="")
#         print("\r")
# parallel(5)

#recurson

# def exfunc(n):
#     return exfunc(n-1)
# exfunc(5)


