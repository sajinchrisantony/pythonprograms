fixed_amount=10000
withdraw=int(input("enter withdraw"))
if withdraw<=fixed_amount:
    balance=fixed_amount-withdraw
    print("balance",balance)
else:
    print("insufficient")
