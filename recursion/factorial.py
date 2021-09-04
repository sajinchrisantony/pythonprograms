def factorial(x):
    if x==0:
        return 1
    else:
        return x * factorial(x-1)
num=int(input("Enter no"))
print(factorial(num))

