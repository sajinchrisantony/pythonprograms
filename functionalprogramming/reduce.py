lst=[1,2,3,4,5,6]

from functools import reduce
total=reduce(lambda num1,num2:num1+num2,lst)
print(total)

#largrst

low=reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)
print(low)

