# lst=[2,4,6] #[10,8,6]
# lst1=[]
# #lst=[3,5,7] #[12,10,8]
# sum=0
# for i in lst:
#     sum+=i
# for i in lst:
#     a=sum-i
#    lst1.append(a)

#print(lst1)

lst=[2,4,6]
# total=sum(lst)
# op=[total-num for num in lst]
# print(op)

print(list(map(lambda num:sum(lst)-num,lst)))

#sum of pairs

#lst=[2,3,4,5] #6 (2,6) 7(3,4)(2,5)

#method 1
# lst=[2,1,3,7,5,4]
# a=int(input("Enter"))
# for i in lst:
#     for j in lst:
#         if(i!=j):
#             if(a==(i+j)):
#                 print(i,j)

#method 2

# lst=[2,1,3,7,5]
# low=0
# upp=len(lst)-1
# a=int(input("Enter"))
# pairs=[]
# while(low<upp):
#     sum=lst[low]+lst[upp]
#     if sum==a:
#         pairs.append((lst[low],lst[upp]))
#         low+=1
#     elif sum>a:
#         upp-=1
#     elif sum<a:
#         low+=1

#print(pairs)

lst=[10,11,12,20,21,10]
lst1=[20,21,22,23,23,30]
#find common elements from both list