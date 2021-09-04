# def printval(*args):
#     return(args)
# print(printval(3,4,6,7,9))
# *args out in tuple

# def details(**args):
#     return args
# print(details(name="anu",age=23,place="kochi"))
#  **args out in dictionary type

#return sum in *args

def printval(*args):
    sum=0
    for i in args:
        sum+=i
    return(sum)
print(printval(1,2,3,4,5))
