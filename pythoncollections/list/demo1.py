#list
#keeping order
#support duplicate elements
#heterogenous

# lst=[1,2,3,4,5]
# print(lst)
# print(type(lst))
# for i in lst:
#     print(i)
# lst2=[1,"hello",3.0,True]
# print(lst2)

# lst1=[]
# print(lst1)
# lst1.append(8)
# lst1.append(8)
# lst1.append("hello")
# print(lst1)

# a=int(input("Enter no"))
# b=[]
# for i in range(a):
#     c=int(input("enter"))
#     b.append(c)
#
# print(b)

#nesting possible
# lst=[1,2,[3,4,5,[1]],6]
# print(lst)

#list is mutable
# lst=[1,2,3]
# lst.append(4)
# lst.remove(2) #remove specific element
# lst.clear() #remove all elements
# print(lst)
# del lst  #delete list
# print(lst)

#squares of elements
# lst=[1,2,3,4,5,6,7]
# lst1=[]
# for i in lst:
#     lst1.append(i**2)
# print(lst1)


#linear search

# def lsearch(lst):
#  n=int(input("Enter element"))
#  flag=0
#  for i in lst:
#     if i==n:
#      flag=1
#      break
#  if flag==1:
#     print(" present")
#  else:
#      print("not present")
# lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# lsearch(lst1)

#sum of elements

# def sum(lst1):
#   sum1=0
#   for i in lst1:
#          sum1+=i
#   print(sum1)
# lst=[1,2,3,4,5,6,7,8,9,10]
# sum(lst)



# lst=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in lst:
#     sum+=i
# print(sum)


#indexing
# lst=[1,2,3,4,5,6,7]
# #     0,1,2.....-2,-1
#
# print(lst[0])
# print(lst[2])
# print(lst[-1])
# print(lst[-3])

#list sorting
# list1=[]
# list=[2,8,1,-4,34,67,-77,8]
# while list:
#     min=list[0]
#     for i in list:
#      if i < min:
#         min=i
#     list1.append(min)
#     list.remove(min)
#
# print(list)
# print(list1)

# def sort(lst):
#     for i in range(len(lst)-1):
#         pos=i
#         for j in range(i,len(lst)):
#             if lst[j]<lst[pos]:
#                 pos=j
#         temp=lst[i]
#         lst[i]=lst[pos]
#         lst[pos]=temp
# lst=[56,77,-9,78,22]

# sort(lst)

# print(lst)

#slicing
# l=[1,2,3,4,5,6,7]
# #  0 1 2 3 4 5 6
# print(l[1:3])
# print(l[-4:-1])
# print(l[:4])
# print(l[3:])
# print(l[:])
# print(l[1:6:2])
# print(l[::-1])

#find duplicate elements

# a=[]
# b=[]
# a1=int(input("Enter range"))
# for i in range(a1):
#    b1=int(input("Enter"))
#    a.append(b1)
# for i in a:
#    if i not in b:
#       b.append(i)
#    else:
#       print(i)
#
# print(a,b)

# find min and max

# a=[1,2,3,4,5,6,7,8,9,10]
#
# a.sort()
# print(a)
# print(a[0])
# print(a[-1])



#list comprehension
# a=[1,2,3,4,5,6,7,8,9,10]
# b=[]
# for i in a:
#     b.append(i*5)
# print(b)

#List comprehensions are used for creating new lists from other iterables
#As list comprehensions return lists,they consist of brackets
# containing expressions which is executed for each element
# along with the for loop to iterate over each element
#

# a=[1,2,3]
# s=[n*5 for n in a]
# print(s)

#even odd using list comprehension
# numbers=[1,2,3,4,5,6,7,8,9,10]
# odd=[i for i in numbers if i%2!=0]
# even=[i for i in numbers if i%2==0]
# print(even)
# print(odd)

# # even numbers between 100 and 200
#
# even=[i for i in range(100,200) if i%2==0]
# print(even)

#multiply
# a=[1,2,3,4,5,6]
# mult=1
# for i in a:
#  mult=mult*i
# print(mult)

#binary search

# a=[45,22,67,89,12,33,55,34,76,77]
# def bsearch():
#  a.sort()
#  print(a)
#  e=int(input("Enter element"))
#  f=0
#  l=len(a)-1
#  flag=0

#  while f<=l:
#     mid = (f + l)//2
#
#     if e>a[mid]:
#         f=mid+1
#     elif e<a[mid]:
#         l=mid-1
#     elif e==a[mid]:
#         flag=1
#         break
#  if flag==1:
#      print(mid,"found")
#  else:
#      print("not found")
# bsearch()

#index updating

# a=[1,2,3]
# print(a)
# a[1]=4
# print(a)


# a=["ab","bc"]
# b=[1,2]
# #a.append(b)
# #print(a)
# a.extend(b)
# print(a)



