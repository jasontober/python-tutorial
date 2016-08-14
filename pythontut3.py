# math strings exception

'''
while True:

    try:
        number = int(input("Please enter a number : "))
        break

    except ValueError:
        print("You didn't enter a number.")

    except:
        print("An unknown error occurred")

print("Thank you for entering a number")
'''

# implement a do-while loop
'''
do
    ... bunch of code
while (condition)

Guess a number between 1 and 10 : 1
Guess a number between 1 and 10 : 7
You guessed correctly!

'''
'''
import random
# generate random number
rand_number = random.randrange(1,11)

# game loop
while True:
    # take user input
    try:
        number = int(input("Guess a number between 1 and 10 : "))
        # check if user won game and whether value was within correct range
        if (number == rand_number):
            print("You guessed correctly!")
            break
        elif ((number < 1) or (number > 10)):
            print("Your guess was out of range! Try again!")
    # handle incorrect input
    except ValueError:
        print("You didn't enter a number.")
    # handle unknown exception
    except:
        print("An unknown error occurred")

print("Thank you for playing!")
'''
'''
import math

# because you used import you access methods by referencing the module
print("ceil(4.4) = ", math.ceil(4.4))
print("floor(4.4) = ", math.floor(4.4))
print("fabs(-4.4) = ", math.fabs(-4.4))

# Factorial = 1 * 2 * 3 * 4
print("factorial(4.4) = ", math.factorial(4))

# return remainder of division
print("fmod(5,4) = ", math.fmod(5,4))

# receive a float and return an int
print("trunc(4.4) = ", math.trunc(4.4))

# return x^y
print("pow(2,2) = ", math.pow(2,2))

# return square root
print("sqrt(4) = ", math.sqrt(4))

# special values
print("math.e = ", math.e)
print("math.pi = ", math.pi)

# return e^x
print("exp(4) = ", math.exp(4))

# return the natural logarithm e * e * e ~= 20 s long log(20) tells
# you that e^3 tells you ~= 20
print("log(20) = ", math.log(20))

# you can define the bas and 10^3 = 1000
print("log(1000,10) = ", math.log(1000,10))

# you can also use base 10 like this
print("log(1000) = ", math.log(1000))

# we have the following trig functions
# sin(x), cos, tan, asin, acos, atan, atan2, asinh, acosh,
# atanh, sinh, cosh, tanh

#convert radians to degrees and vice versa
print("degrees(1.5708) = ", math.degrees(1.5708))
print("radians(90) = ", math.radians(90))
'''


''' decimal module

from decimal import Decimal as D

sum = D(0)
sum += D("0.1")
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3")
print("Sum = ", sum)

print(".1 + .1 + .1 - .3 = ", .1 + .1 + .1 - .3)
'''
'''
samp_string = "This is a very important string"

print(samp_string[0])
print(samp_string[-1])
print("length = ", len(samp_string))
print(samp_string[:4])
print(samp_string[8:])
print("Green " + "Eggs")
print("Hello " * 5)
num_string = str(4)
print(num_string)

for char in samp_string:
    print(char)

for i in range(0, len(samp_string)-1, 2):
    print(samp_string[i] + samp_string[i+1])

#A - Z 65 - 90
#a - z 97 - 122
print ("A = ", ord("A"))
print("65 = ", chr(65))
'''

'''
# receive uppercase string - translate to unicode - translate back

# Enter a string to hide in uppercase :
# convert into unicode numbers
# print out Secret Message :
# print out original message

# get user input
message = input("Enter a string: ")

# convert message to unicode
secretMessage = ''
for char in message:
    secretMessage += str(ord(char) - 23)

# print message to console
print("Secret Message : ", secretMessage)

# convert back to uppercase
originalMessage = ''
for i in range(0, len(secretMessage)-1, 2):
    char_code = secretMessage[i] + secretMessage[i+1]
    originalMessage += chr(int(char_code) + 23)

""" -- harder way
i = 0
while i < len(secretMessage):
    char_code = int(secretMessage[i] + secretMessage[i+1])
    #print(char_code)
    if ((char_code >= 65) and (char_code <= 99)):
        #print(char_code)
        originalMessage += chr(char_code)
    else:
        char_code = int(secretMessage[i] + secretMessage[i+1] + secretMessage[i+2])
        #print(char_code)
        originalMessage += chr(char_code)
        i += 3
        continue
    i += 2
"""

# print original message to console
print("Original message = ", originalMessage)
'''