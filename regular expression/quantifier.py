# import re
# x="a+" #a including group
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print ( match.group () )
#

# import re
# x="a*" #count including zero number of a
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print ( match.group () )

# import re
# x="a?" #count a as each including zero number of a
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print (match.group())


# import re
# x="a{2}" #no of position
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print (match.group())

# import re
# x="a{2,3}" #minimum 2 a and maximum 3 a
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print (match.group())

# import re
# x="^a" #check starting with a
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print (match.group())

# import re
# x="a$" #check ending with a
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print (match.group())

# import re
#
# n="hello"
# x='[a-z]+'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")

# import re
#
# n="56gk"
# x='[0-9]{2}[a-z]{2}'
# #x='[0-9]{2}[k][g]'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")

#phone number validation

# import re
#
# n=input("Enter number to validate")
# x='\d{10}'
# #x='[0-9]{10}'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")

#indian no +911234567890

#import re

# n=input("Enter number to validate")
# x='[+][9][1]\d{10}$'
# #$ for ending , even if not there no problem
# match=re.fullmatch(x,n)
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")

#vehicle reg no validation KL01AA1234
#import re

# n=input("Enter vehicle reg no")
# x='[A-Z]{2}\d{2}[A-Z]{2}\d{4}$'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")

#combination of uppercase and lowercase letters
#ending with a number

#import re

# n=input("Enter")
# x='[A-Za-z]+\d$'
# #d without number is default 1
# match=re.fullmatch(x,n)
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")

#email validation

#import re

# n=input("Enter")
# x='[A-Za-z0-9]+[@][A-Za-z0-9]+[.][a-z]{2,3}$'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")

#start with a end with b

import re
n=input("Enter")
#\W special characters , '*' can come or not come , '+' 1 come
x='^a[a-zA-Z0-9\W]*b$'
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("Invalid")

#minimum length 8 max 15 , no numbers

# import re
# n=input("Enter")
# #\D except digits
# x='[\D]{8,15}'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")
#
#starting with uppercase letter then numbers,lowercase,symbols

# import re
#
# n = input("Enter")
#
# x = '^[A-Z][a-z0-9\W]*'
# match = re.fullmatch(x, n)
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")
