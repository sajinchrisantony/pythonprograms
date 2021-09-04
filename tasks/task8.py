#student grade

m1=int(input("Enter mark 1"))
m2=int(input("Enter mark 2"))
m3=int(input("Enter mark 3"))
m4=int(input("Enter mark 4"))
m5=int(input("Enter mark 5"))

total=m1+m2+m3+m4+m5
avg=total/5

if avg>=90:
    grade="A"
elif 80<=avg<90:
    grade="B+"
elif 70<=avg<80:
    grade = "B"
elif 60<=avg<70:
    grade = "C+"
elif 50<=avg<60:
    grade = "C"
elif 45<=avg<50:
    grade = "D"
else: grade="E"

print(m1,m2,m3,m4,m5)
print(avg)
print("Grade=",grade)