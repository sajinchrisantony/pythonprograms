# for i in "hello":
#     print(i)
#
# a="why"
# for i in a:
#     print(i)

#in ==
#not in !=
#common and non common elements
# a="abcd"
# b="acfg"
#
# for i in a:
#     if i not in b:
#             print(i)

#string copy
# a="abcd"
# b=""
# for i in a:
#     b=b+i
# print(b)

#present
# a="luminar"
# flag=0
# b=input("Enter character")
#
# for i in a:
#     if i in b:
#         flag=1
# if flag==1:
#     print("present")
# else:
#     print("Not present")

#lettter count
# a="malayalam"
# b=input("Enter ch")
# count=0
# for i in a:
#     if i in b:
#         count+=1
# print(count)

#remove punctutation
# punc="!@#$%^&*()"
# a=input("enter string")
#
# nop=""
#
# for i in a:
#     if i not in punc:
#         nop+=i
# print(nop)

#no of vowels
#vow="aeiou"
# a=input("Enter")
# count=0
# for i in a:
#     if i in "AEIOUaeiou":
#         count+=1
#         print(i)
# print(count)

#print 1st recursive character
# a=input("Enter")
# b=""
# for i in a:
#     if i not in b:
#         b=b+i
#     else:
#         print(i)
#         break

a=input("enter lower")
#print(a.upper())
b=a.upper()
print(b)
c=input("Enter upper")
d=c.lower()
print(d)
