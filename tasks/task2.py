#swapping

#1.using temporary variable
no1=5
no2=6
print(no1,no2)

swap=no1


no1=no2
no2=swap

print(no1,no2)

#assignment approach

(no1,no2)=(no2,no1)
print(no1,no2)

no1=no1+no2
no2=no1-no2
no1=no1-no2
print(no1,no2)