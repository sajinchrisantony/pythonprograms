employees = [
    {"e_id": 1000, "e_name": "ram", "salary": 25000, "department": "testing", "exp": 1},
    {"e_id": 1001, "e_name": "ravi", "salary": 22000, "department": "ba", "exp": 1},
    {"e_id": 1002, "e_name": "raj", "salary": 20000, "department": "mrkt", "exp": 1},
    {"e_id": 1003, "e_name": "nikil", "salary": 26000, "department": "developer", "exp": 1},
    {"e_id": 1004, "e_name": "nivi", "salary": 28000, "department": "developer", "exp": 2},

]

#print employee names only
#case 1

# for employee in employees:
#     print(employee["e_name"])

#using map
# e_names=list(map(lambda employee:employee["e_name"],employees))
# print(e_names)

#print employee names in uppercase
#case 1

# for employee in employees:
#     print(employee["e_name"].upper())

#using map
# e_upper=list(map(lambda emp:emp["e_name"].upper(),employees))
# print(e_upper)


#print employee working as developer
#case2

# for employee in employees:
#     if(employee["department"]=="developer"):
#      print(employee["e_name"])

#using filter 1
developers=list(filter(lambda emp:emp["department"]=="developer",employees))
developers_name=list(map(lambda developer:developer["e_name"],developers))
print(developers_name)

#using filter 2

developers_name=list(map(lambda developer:developer["e_name"],list(filter(lambda emp:emp["department"]=="developer",employees))))
print(developers_name)

#total salary
#case3

# total=0
# for employee in employees:
#     total+=employee["salary"]
# print(total)

#using reduce
#from functools import reduce


#case1 map
# case2 filter
#case 3 reduce

#print employee names whose name starting with a
#case2 filter
