# functions
"""
def add_numbers(num1, num2):
    return num1 + num2

print("5 + 4 = ", add_numbers(5,4))


def assign_name():
    name = "Doug"

print("Name is : ", assign_name())


def change_name():
    #name = "Mark"
    #return "Mark"
    global gbl_name
    gbl_name = "Sammy"

#name = "Tom"

#name = change_name(name)
change_name()

#print("Name is : ", name)
print("Name is : ", gbl_name)


def get_sum(num1, num2):
    sum = num1 + num2

print(get_sum(5, 4))
"""

# solve for x
# x + 4 = 9

# x will always be the 1st value received and you only will deal with addition
""" - my solution
def solve_for_x(equation):
    num1 = 0
    num2 = 0
    # parse equation to get values
    for char in equation:
        if char.isdigit():
            if num1 == 0:
                num1 = int(char)
            elif num2 == 0:
                num2 = int(char)

    # return solution
    return num2 - num1

# prompt user for equation
equation = input("Please enter an equation : ")

# print result
print(equation)
print("x = ", solve_for_x(equation))
"""

"""
# solve for x
# x + 4 = 9

# x will always be the 1st value received and you only will deal with addition

# receive the string and split the string into variables
def solve_equation(equation):
    x, add, num1, equals, num2 = equation.split()
# convert the strings in ints (the numbers)
    num1, num2 = int(num1), int(num2)
# convert the result into a string and join it to the string "X = "
    return "X = " + str(num2 - num1)

# print()
print(solve_equation("x + 4 = 9"))
"""

"""
def mult_divide(num1, num2):
    return (num1 * num2), (num1 / num2)

mult, divide = mult_divide(4, 5)

print("4 * 5 ", mult)
print("4 / 5 ", divide)
"""

# list of primes
# a prime can only be divided by 1 and itself
# 5 is a prime 1 and 5 = positive factor
# 6 is not prime 1, 2, 3, 6

"""
def primes(limit):
    prime_list = []
    if (limit <= 1):
        return prime_list
    else:
        for i in range(2, limit+1):
            for j in range(i-1, 1, -1):
                # print("i = " , i,"   j  = ", j, "   mod = ", (i%j))
                if ((i % j) == 0):
                    # print("divisible")
                    break
                if (j == 2):
                    prime_list.append(i)
    return prime_list

# prompt user for maximum value
while True:
    try:
        limit = int(input("Please enter the highest value for primes desired : "))
        break
    except ValueError:
        print("Value was not a whole number.")
    except:
        print("Unknown Error")

# return list of primes
print(primes(limit))



def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True


def get_primes(max_number):

    prime_list = []

    for num1 in range(2, max_number):
        if is_prime(num1):
            prime_list.append(num1)

    return prime_list


# prompt user for maximum value
while True:
    try:
        limit = int(input("Please enter the highest value for primes desired : "))
        break
    except ValueError:
        print("Value was not a whole number.")
    except:
        print("Unknown Error")

list_of_primes = get_primes(limit)

for prime in list_of_primes:
    print(prime)
"""

"""
def sum_all(*args):
    sum = 0

    for i in args:
        sum += i

    return sum

print("Sum = ", sum_all(1,2,3,4,5,3,2,2))
"""



# create program that allows the user to calculate the area for different shapes
import math


def calc_circle_area(radius):
    return math.pi * math.pow(radius, 2)


def get_circle_area():
    while True:
        try:
            radius = float(input("Please enter the radius of the circle : "))
            break
        except ValueError:
            print("Not a valid value.")
        except:
            print("Unknown error")
    print("A circle with radius {} has an area of {:.2f}".format(radius, calc_circle_area(radius)))


def calc_rectangle_area(height, width):
    return height * width


def get_rectangle_area():
    while True:
        try:
            height = float(input("Please enter the height of the rectangle : "))
            width = float(input("Please enter the width of the rectangle : "))
            break
        except ValueError:
            print("Not valid values.")
        except:
            print("Unknown error")
    print("A rectangle with height {} and width {} has an ara of {:.2f}".format(height, width, calc_rectangle_area(height, width)))


def calc_parallelogram_area(height, base):
    return height * base


def get_parallelogram_area():
    while True:
        try:
            height = float(input("Please enter the height of the parallelogram : "))
            base = float(input("Please enter the base of the parallelogram : "))
            break
        except ValueError:
            print("Not valid values.")
        except:
            print("Unknown error")
    print("A parallelogram with height {} and width {} has an ara of {:.2f}".format(height, base, calc_parallelogram_area(height, base)))


def calc_rhombus_area(height, base):
    return height * base


def get_rhombus_area():
    while True:
        try:
            height = float(input("Please enter the height of the parallelogram : "))
            base = float(input("Please enter the base of the parallelogram : "))
            break
        except ValueError:
            print("Not valid values.")
        except:
            print("Unknown error")
    print("A parallelogram with height {} and width {} has an ara of {:.2f}".format(height, base, calc_rhombus_area(height, base)))


def get_area(shape):
    shape = shape.lower()

    if shape == "circle":
        get_circle_area()
    elif shape == "rectangle":
        get_rectangle_area()
    elif shape == "parallelogram":
        get_parallelogram_area()
    elif shape == "rhombus":
        get_rhombus_area()
    elif shape == "triangle":
        get_triangle_area()
    elif shape == "trapezoid":
        get_trapezoid_area()
    else:
        print("Unsupported shape type")


def main():
    shape_type = input("Get area for what shape (circle/rectangle/parallelogram/rhombus/triangle/trapezoid) : ")
    get_area(shape_type)


main()