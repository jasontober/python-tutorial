# dictionaries and recursive functions
"""
derekDict = {"fName" : "Derek", "lName": "Banas",
             "address" : "123 Main St"}

print("My Name :", derekDict["fName"])

derekDict["address"] = "215 North St"

derekDict["city"] = "Pittsburg"

print("Is there a city: ", "city" in derekDict)

print(derekDict.values())

print(derekDict.keys())

for k, v in derekDict.items():
    print(k, v)

print(derekDict.get("lName", "Not Here"))

del derekDict["fName"]

for i in derekDict:
    print(i)

# derekDict.clear()

# for i in derekDict:
#     print(i)

employees = []

fName, lName = input("Enter Employee Name : ").split()

employees.append({"fName" : fName, "lName" : lName})

print(employees)
"""

# create a customer list
# array of customer dictionaries
"""
Enter Customer (Yes/No) : y
Enter Customer Name : Derek Banas
Enter Customer (Yes/No) : y
Enter Customer Name : Sally Smith
Enter Customer (Yes/No) : n
Derek Banas
Sally Smith
"""
"""
# create list
customers = []
# program loop
while True:
    # prompt user for customer entry
    userChoice = input("Enter Customer (Yes/No) : ")
    userChoice = userChoice[0].lower()
    if userChoice == "y":
        # print("yes")
        # prompt user for customer name
        fName, lName = input("Enter Customer Name : ").split()
        # print("First Name = {}\tLast Name = {}".format(fName, lName))
        # add customer name as dictionary
        customers.append({'fName"': fName, 'lName': lName})
    elif userChoice == "n":
        # print("no")
        break
    else:
        print("Invalid entry. Please enter Yes or No.")

# print customer list
for k in customers:
    print(k['fName'], k['lName'])
"""
"""
# 3! = 3 * 2 * 1

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)

print("4! = ", factorial(4))
"""
# fibonacci numbers
# 0,1,1,2,3,5,8,13,21,34,55
# F(n) = F(n-1) + F(n-2)
# Where F0 = 0 and F1 = 1


def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)

for i in range(10):
    print(fibonacci(i))