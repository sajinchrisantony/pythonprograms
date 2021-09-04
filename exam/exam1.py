#2. lst = [1, 0, 7, 5, 9, 2, 3, 5, 7, 2, 0, 1, 10]
#    #    \  \  \  \  \  \  \                 \
# # b=[]
# #
# # for i in lst:
# #     if i not in b:
# #         b.append(i)
# #     else:
# #         lst.remove(i)
# # print(lst)
# # print(b)
#
# b=[b.append(i)  for i in lst if i not in b]

a=[1,0,7,5,9,2,3,5,7,2,0,1,10]

b=[]
b=[b.append(i) for i in a if i not in b]
print(b)


# 3.
a=[3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
a.sort()
print(a)
print("Second Largest is ",a[-2])

# 4.
#
a=[1,2,3,45,6,7,33,11,77,9,0,5]
b=[3,77,0,5,33,6,22,5,90,32,56,78,98,54,67,11,34,88]
print("The common elements are ")
for i in a:
    if i in b:
        print(i)

5.

def add(a,b):
 s=a+b
 return(s)

def sub(a,b):
 s=a-b
 return(s)

def mult(a,b):
 s=a*b
 return(s)

def div(a,b):
 s=a/b
 return(s)

def fd(a,b):
 s=a//b
 return(s)

def rem(a,b):
 s=a%b
 return(s)

def exp(a,b):
 s=a**b
 return(s)

print("*********************CALCULATOR***********************")

a=int(input("Enter number 1   "))
sym=input("Enter + , - , * , / , // ,  %  , **   ")
b=int(input("Enter number 2   "))

if sym=='+':
    print(add(a,b))

elif sym=='-':
    print(sub(a,b))

elif sym=='*':
    print(mult(a,b))

elif sym=='/':
    print(div(a,b))

elif sym=='//':
    print(fd(a,b))

elif sym=='%':
    print(rem(a,b))

elif sym=='**':
    print(exp(a,b))

else:
    print("Enter correct symbol")
#
#

# 6.
#
def prime(a,b):
 b1=[]
 for i in range(a+1,b+1):
     for j in range(2,i):
            if i % j ==0:
                break
     else:
         b1.append(i)
 print(b1)
 sum=0
 for k in b1:
    sum+=k
 return(sum)

print(prime(1,50))


7.

a=input("Enter string")
b=['a','e','i','o','u']
c=[]
for i in a:
    if i not in b:
        c.append(i)
print(c)


10.

a=[i for i in range(1,101) if i%5==0]
print(a)

11.

a=[1,2,3,4,5]
b=[7,8,9]

a.append(6)
print(a)
a.extend(b)
print(a)
