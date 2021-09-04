#sets... to store elements

# a={1,2,3,4,5}
# print("a=",a)
# print("a is ",type(a))
# b={5,6,7,8,9}
# print(b)

#set is heterogenous , different types of elements can be stored
# a=set()
# a.add(2)
# a.add(4)
# a.add(7)
# a.add("hello")
# a.add(7.8)
# a.add(True)
# print(a)
#
# b={7,2,5,9,4,6,10,3}
# # sets doesnt keep order
# print(b)
#
# a={1,2,5,3,7,3,2,7}
# #set doesnt support duplicate elements
# print(a)
#
# b={1,"hello",6,5,7,5.6,False}
# print(b)
# for i in b:
#     print(i)

#get no of elements get elements print set

# a=int(input("Enter no"))
# b=set()
# for i in range(a):
#     c=int(input("Enter"))
#     b.add(c)
# print(b)

#set a={1,2,3,4,5,6,7,8,9}
#print set b with squares of a

# a={1,2,3,4,5,6,7,8,9}
# b=set()
# for i in a:
#     b.add(i**2)
# print(b)


# a=int(input("Enter"))
# b=set()
# for i in range(a):
#     c=int(input("Enter"))
#     b.add(c)
# d=set()
# for i in b:
#     d.add(i**2)
# print(d)

#set is mutable which is updating can be done ,can be removed

# s={1,2,3,4,5,6,7,8,9}
# s.remove(2)
# print(s)
#
# #deleting all elements
# s.clear()
# print(s)
#
# #deleting set
# del s
# print(s)

# set
# 1.not keeping order
# 2.not support duplicate elements
# 3.heterogenous
# 4.mutable

# a={1,{2,3}}
# print(a)
# 5.nesting not possible

#print even and odd set
# a={51,878,65,654,84,9841,84984,6548}
# b=set()
# c=set()
# for i in a:
#     if i%2==0:
#         b.add(i)
#     else:
#         c.add(i)
# print(b,c)

#print common elements
# a={1,2,3,4,5,6,22,0}
# b={11,43,1,67,44,0}
# c=set()
# for i in a:
#         if i in b:
#             c.add(i)
# print(c)

#union,interesection,difference

# a={1,2,3,4,5,6,7}
# b={1,2}
# print(a.union(b)) #total elements
# print(a.intersection(b)) #common elements
# print(a.difference(b))   #a-b

#prime and non prime

s={5,6}
a=set()
b=set()
for i in s:
 if i>=1:
    for j in range(2,i):
        if i%j==0:
            b.add(i)
            break
    else:
        a.add(i)
print(a,b)





