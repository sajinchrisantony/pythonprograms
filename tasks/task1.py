#average marks

print("Enter your mark of 5 subjects")
#int(input(m1,m2,m3,m4,m5))
m1=int(input("subject 1"))
m2=int(input("subject 2"))
m3=int(input("subject 3"))
m4=int(input("subject 4"))
m5=int(input("subject 5"))
print("subject 1",m1,"subject 2",m2,"subject 3",m3,"subject 4",m4,"subject 5",m5)

total=m1+m2+m3+m4+m5
print("Total Marks=",total)

avg=total/5
print("Average=",avg)
