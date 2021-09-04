a=int(input("no 1"))
b=int(input("no 2"))
c=int(input("no 3"))

if a>b and a>c:
    print("a greater")
elif a>b and a<c:
    print("c greater")
elif b>a and b>c:
    print("b greater")
elif a==b==c:
    print("equal")
else:
    print("c greater")