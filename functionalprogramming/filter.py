lst=[2,3,4,5,6]

#even nos

evens=list(filter(lambda num:num%2==0,lst))
print(evens)


odd=list(filter(lambda num:num%2!=0,lst))
print(odd)
