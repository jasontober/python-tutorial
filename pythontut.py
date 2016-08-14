# Learn to program

""" first example
# Ask the user to input their name and assign it to a variable named "name"

name = input('What is your name')

# Print out hello followed by the name they entered

print('Hello', name)
"""
""" second example
# Ask the user to input 2 values and store them in variables num1 and num2

num1, num2 = input('Enter two numbers:').split()

# Convert the strings into regular Integers

num1 = int(num1)
num2 = int(num2)

# Add the values entered and store in a variable named sum

sum = num1 + num2

# subtract the values ane store in a variable named difference

difference = num1 - num2

# multiple the vales and store in a variable named product

product = num1 * num2

# divide the values and store in a variable name quotient

quotient = num1 / num2

# use modulus on the values to find the remainder

remainder = num1 % num2

# print the results on the screen for the user
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
"""
"""first problem
# problem: Receive miles and convert to kilometers
# kilometers = miles * 1.60934
# enter miles 5
# 5 miles equals 8.14 kilometers

# Ask the user to input miles and assign it to the miles variable
miles = input('Enter miles')

# convert from strint to int
miles = int(miles)

# calculate kilometers
kilometers = miles * 1.60934

# print results using format()
print("{} miles equals {} kilometers".format(miles, kilometers))
"""
"""
# enter Calculation: 5 * 6
# 5 * 6 = 30

# store the user input of 2 numbers and operator of choice

num1, operator, num2 = input("Enter calculation: ").split()

# convert strings into integer

num1 = int(num1)
num2 = int(num2)

# if  + then we need to provide output based on addition

if (operator == '+'):
    result = num1 + num2
elif (operator == '-'):
    result = num1 - num2
elif (operator == '*'):
    result = num1 * num2
elif (operator == '/'):
    result = num1 / num2
else:
    result = 0
    print("invalid operator {}".format(operator))

# print the result
print("{} {} {} = {}".format(num1, operator, num2, result))
"""
"""
# We'll provide different output based on age
# 1-18 -> important
# 21, 50, >65 -> important
# all others -> not important

# Receive age and store in age

age = eval(input("Enter age: "))

# if age is both greater than  or equal to 1 and less than 18, print Important

if ((age >= 1) and (age <= 18)):
    print("Important")

# if age is either 21 or 50 Important
elif ((age == 21) or (age == 50)):
    print("Important")

# if age is less than 65 and then convert true to false and vice versa
elif not(age < 65):
    print("Important")

# else not important
else:
    print("Not Important Birthday")
"""
# if age is 5 - go to kindergarten
# ages 6-17 goes to grades 1-12
# if age is greater than 17 go to college
# try to complete with 10 or less lines

age = eval(input("Enter your age: "))

if (age < 5): print("Stay home")
elif (age == 5): print("Go to kindergarten")
elif ((age >= 6) and (age <= 17)): print("Go to grade {}".format(age-5))
elif ((age >= 18) and (age <= 21)): print("Go to college")
else: print("Go to work")

