class Student:
    def __init__(self,nm,id,dp,mk):
        self.nm=nm
        self.id=id
        self.dp=dp
        self.mk=mk

    def printvalue(self):
        print("name::",self.nm)
        print("id::",self.id)
        print("department::",self.dp)
        print("mark::",self.mk)

    def __str__(self):
        return self.nm

f1=open("wrk",'r')
for line in f1:
    l=line.split(",")
    name=l[0]
    age=l[1]
    dept=l[2]
    mark=l[3]
    st=Student(name,age,dept,mark)
    print(st)
    st.printvalue()