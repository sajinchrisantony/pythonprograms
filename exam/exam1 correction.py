#1
# a=int(input("Enter initial"))
# b=int(input("Enter final"))
#
# r=5
# for i in range(a,b):
#     if(i%2==0):
#         for k in range(r,0,-1):
#             for j in range(0,k):
#                 print(i,end=" ")
#
#             print("\r")
#     else:
#         for l in range(r):
#             for n in range(0,l+1):
#                 print(i,end=" ")
#             print("\r")
#2

a=[1,0,7,5,9,2,3,5,7,2,0,1,10]

print(list(set(a)))
#6.
# def sumprime(min,max):
#    sum=0
#    for a in range(min,max):
#        if a>1:
#            for i in range(2,a):
#                if a%i==0:
#                    break
#            else:
#                sum+=a
#    return sum
#
# print(sumprime(1,10))

#7.