# functions as objects, function annotations, lambda anonymous functions, Map, Filter, reduce and a bunch of problems

"""
def mult_by_2(num):

    return num * 2

times_two = mult_by_2

print("4 * 2 = ", times_two(4))


def do_math(func, num):
    return func(num)

print("8 * 2 = ", do_math(mult_by_2, 8))

def get_func_mult_by_num(num):

    def mult_by(value):
        return num * value

    return mult_by


generated_func = get_func_mult_by_num(5)

print("5 * 10 = ", generated_func(10))

listOfFuncs = [times_two, generated_func]

print("5 * 9 = ", listOfFuncs[1](9))
"""

"""
# --------Problem----------
# Create a function that receives a list and a function
# The function passed will return True or False if a list
# value is odd.
# The surrounding function will return a list of odd
# numbers

# create function to determine odd numbers
def odd_numb(num):
    return (num % 2) == 1

# print("3 is odd : ", odd_numb(3))
# print("2 is odd : ", odd_numb(2))


def create_list_of_odds(list, funct):

    odd_list = []

    for i in list:
        if funct(i):
            odd_list.append(i)

    return odd_list


def main():

    num_list = list(range(100))

    odd_list = create_list_of_odds(num_list, odd_numb)

    print("List of Odd numbers : ")
    for i in odd_list:
        print(i)
    print()

main()
"""

"""
# function annotations
def random_func(name: str, age: int, weight: float) -> str:
    print("Name : ", name)
    print("Age : ", age)
    print("Weight : ", weight)

    return "{} is {} years old and weighs {}".format(name, age, weight)

print(random_func("Derek", 41, 165.5))
print(random_func(89, "Derek", 'Turtle'))
print(random_func.__annotations__)
"""


# Anonymous functions using Lambda

# lambda arg1, arg2, ..... : expression use the arguments

"""
sum = lambda x, y: x + y

print("Sum : ", sum(4,5))

can_vote = lambda age: True if age >= 18 else False

print("Can Vote :  ", can_vote(19))

powerList = [lambda x: x ** 2,
             lambda x: x ** 3,
             lambda x: x ** 4]

for func in powerList:
    print(func(4))

import random

attack = {'quick': (lambda: print("Quick Attack")),
          'power': (lambda: print("Power Attack")),
          'miss': (lambda: print("Missed Attack"))}

attack["quick"]()

attackKey = random.choice(list(attack.keys()))

attack[attackKey]()
"""


# --------Problem----------
# Create a random list filled with the characters H and T
# for heads and tails. Output the number of Hs and Ts
# Example Output
# Heads : 46
# Tails : 54

import random

"""
coinFlip = {'Heads': (lambda: 'H'),
            'Tails': (lambda: 'T')}

# print("Coin Flip result : ", coinFlip[coinFlipKey]())

# create the variables
randomList = []
headsCount = 0
tailsCount = 0

# populate the list with Hs and Ts
for i in range(100):
    coinFlipKey = random.choice(list(coinFlip.keys()))
    randomList.append(coinFlip[coinFlipKey]())

# print(randomList)

# count results
for i in randomList:
    if i == 'H':
        headsCount += 1
    elif i == 'T':
        tailsCount += 1
    else:
        print("invalid value")

# print the results
print("Heads : ", headsCount)
print("Tails : ", tailsCount)


# create the list
flipList = []

# populate the list with 100 Hs and Ts
for i in range(1000):
    flipList += random.choice(['H', 'T'])

# output the results
print("Heads : {}\nTails : {}".format(flipList.count('H'), flipList.count('T')))
"""

# Map

"""
oneTo10 = range(1, 11)


def dbl_num(num):
    return num * 2


print(list(map(dbl_num, oneTo10)))

print(list(map((lambda x: x * 3), oneTo10)))

aList = list(map((lambda x, y: x + y), [1,2,3], [1,2,3]))

print(aList)



# Filter
print(list(filter((lambda x: x % 2 == 0), range(1, 11))))



# --------Problem----------
# Find the multiples of 9 from a random 100 values list with
# values between 1 and 1000

# import random
import random

# create list
randList = list(random.randint(1, 1001) for i in range(100))

# print output
print(list(filter((lambda x: x % 9 == 0), randList)))
"""

# reduce
from functools import reduce

print(reduce((lambda x, y: x + y), range(1, 6)))