def recur_fibo(n):
    if n<=1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)

nterms=3

print("Fibonacci Sequence")

for i in range(nterms):
    print(recur_fibo(i))

