import re
x='[+][9][1]\d{10}$'
f1=open("phone",'r')
for i in f1:
 number=i.rstrip("\n")
 match=re.fullmatch(x,number)
 if match!=None:
    print(number)
