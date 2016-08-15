# iterables, iterators, list comprehensions, generator functions and generator expressions

# iterables
# store sequence of values
"""
sampStr = iter("Sample")

print("Char :", next(sampStr))
print("Char :", next(sampStr))

class Alphabet:

    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.letters) - 1:
            raise StopIteration
        self.index += 1
        return self.letters[self.index]


alpha = Alphabet()

for letter in alpha:
    print(letter)

derek= {"fName": "Derek", "lName": "Banas"}

for key in derek:
    print(key, derek[key])
"""


# -------------Problem-----------
# Create a class that returns values from the Fibonacci
# sequence each time next is called
# sample Output
# Fib : 1
# Fib : 2
# Fib : 3
# Fib : 5

"""
class FibonacciSequence:

    def __init__(self, limit=10):
        self.limit = limit
        self.index = -1
        self.values = []
        for i in range(self.limit):
            self.values.append(fibonacci(i))
        print(self.values)

    @ staticmethod
    def fibonacci(num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fibonacci(num-1)+fibonacci(num-2)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.values) - 1:
            raise StopIteration
        self.index += 1
        return self.values[self.index]

limit = 10

fib = FibonacciSequence(limit)

for i in range(limit):
    print("Fib :", next(fib))
"""


# list comprehensions
# going to execute a function against an iterable
"""
# maps on left
print(list(map((lambda x: x * 2), range(1, 11))))

print([2 * x for x in range(1, 11)])

# filters on right
print(list(filter((lambda x: x % 2 != 0), range(1, 11))))

print([x for x in range(1, 11) if x % 2 != 0])

# generate 50 values
# take to the power of 2
# return multiples of 8

print([i ** 2 for i in range(50) if i % 8 == 0])

print([x * y for x in range(1, 3) for y in range(11, 16)])

# generate a list of 10 values
# multiply them by 2
# return multiples of 8

print([x for x in [i * 2 for i in range(10)] if x % 8 == 0])
"""

# Problem
# Generate a list of 50 random values between 1 and 1000
# and return those that are multiples of 9
# you'll have to use a list comprehension in a list comprehension
# import random
# print([x for x in [random.randint(1, 1001) for i in range(50)] if x % 9 == 0])
"""
multiList = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

print([col[1] for col in multiList])
print([multiList[i][i] for i in range(len(multiList))])
"""

# generator


def isprime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def gen_primes(max_number):
    for num1 in range(2, max_number):
        if isprime(num1):
            yield num1


prime = gen_primes(50)

print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))



# generator expressions

double = (x * 2 for x in range(10))

print("Double :", next(double))
print("Double :", next(double))
print("Double :", next(double))

for num in double:
    print(num)