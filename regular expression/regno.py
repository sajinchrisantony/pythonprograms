import re
x='[L][U][M]\d{2}[P][Y]\d{3}$'
f2=open("validregno",'w')
f1=open("regno",'r')
for i in f1:
 number=i.rstrip("\n")
 match=re.fullmatch(x,number)
 if match!=None:
    f2.write(number)
    f2.write("\n")


