# tup1=1,2,3,6,0,1,2,3,"hello",True
# print(tup1)
# print(type(tup1))
#
# #immutable
# #keeps order
# #support duplicate elements
# #heterogenous
# #nesting possible
#
# for i in tup1:
#     print(i)

# tup=1,2,3,4,5,6,7,8,9
# print(tup)
# print(max(tup))
# print(min(tup))
# print(len(tup))
# print(tup[0])
# print(tup[-1])
# print(tup[1:4])

# #type of tuples
#
# #empty tuple
# my_tuple=()
# print(my_tuple)
#
# #tuple having integers
# my_tuple=(1,2,3)
# print(my_tuple)
#
# #tuple wit mixed datatpes
# my_tuple=(1,"hello",3,4)
# print(my_tuple)
#
# #nested tuple
# my_tuple=("mouse",[8,4,6],(1,2,3))
# print(my_tuple)
#
# #tuple with one element
# a=2,
# print(a)
# print(type(a))

# tuple=3,4.5,"hello"
# print(tuple)

# #tuple unpacking
# a,b,c=tuple
# print(a)
# print(b)
# print(c)

#sum using tuple unpacking

# tup=1,6,9,10
# a,b,c,d=tup
# sum=a+b+c+d
# print(sum)

# tuple=('a','p','p','l','c')
# print(tuple.count('p'))
# print(tuple.index('p'))

#print details of above 15000
lst=[(1,"anu",28,20000),(2,"vinu",23,15000),(3,"ram",25,10000)]
for i in lst:
    #print(i[3])
    if i[-1] >= 15000:
     print(i)


