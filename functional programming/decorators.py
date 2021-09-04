# def revert_val(func):
#     def wrapper(no1,no2):
#         if no1<no2:
#             (no1,no2)=(no2,no1)
#             return func(no1,no2)
#         else:
#             return func(no1,no2)
#     return wrapper
#
# @revert_val
# def div(num1,num2):
#     return num1/num2
# print(div(2,10))
#
# @revert_val
# def sub(num1,num2):
#     return num1-num2
# print(sub(1,10))

#change pin delete acccount
#
# def admin_required(func):
#     def wrapper(a,b):
#         if a!="admin":
#             raise Exception("You are not allowed")
#         else:
#             return func(a,b)
#     return wrapper
#
# @admin_required
# def change_pin(user,pin):
#     mypin=pin
#     return mypin
#
# @admin_required
# def delete_ac(user,acno):
#     return str(acno)+" delete"
#
# print(change_pin("admin",1000))
# print(delete_ac('admin',10001))

#vaccine 18 above ...

def age_check(func):
    def wrapper(a,b,c):
        if b<18:
            raise Exception("You are not eligible")
        else:
            return func(a,b,c)
    return wrapper

@age_check
def vaccine(name,age,place):
    return str(name)+str(place)+"you can be vaccinated"

print(vaccine("sajin",18,"kochi"))