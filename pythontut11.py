# static, module, and exception handling

# static method allows use without initialization
"""
class Sum:

    @staticmethod
    def getSum(*args):
        sum = 0

        for i in args:
            sum += i

        return sum


def main():

    print("Sum : ", Sum.getSum(1,2,3,4,5))


main()
"""
"""
class Dog:

    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name
        Dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))

def main():

    spot = Dog("Spot")
    doug = Dog("Doug")
    spot.getNumOfDogs()
    doug.getNumOfDogs()

main()
"""
"""
#import getSumModule
from getSumModule import getSum

# print("Sum : ", getSumModule.getSum(1,2,3,4,5))
print("Sum : ", getSum(1,2,3,4,5))
"""

# Exception Handling
"""
try:
    aList = [1,2,3]
    print(aList[3])
except IndexError:
    print("Sorry that index doesn't exist")
except:
    print("Unknown Error")


class DogNameError(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    dogName = input("What is your dog's name : ")

    if any(char.isdigit() for char in dogName):

        raise(DogNameError)
except DogNameError:
    print("Your dog's name cannot contain a number!")


# finally

num1, num2 = input("Enter 2 values to divide : ").split()

try:
    quotient = int(num1)/int(num2)
    print("{} / {} = {}".format(num1, num2, quotient))

except ZeroDivisionError:
    print("You cannot divide by zero")

else:
    print("You didn't raise an exception")

finally:
    print("I execute no matter what")
"""

# 1. create a file named "mydata2.txt"
# 2. use what you learned in part 8 to find out how to open a file without using with
# 3. catch FileNotFoundError
# 4. print contents of the file
# 5. in finally print out some message
# 6. open nonexistent file mydata3.txt


try:
    myFile = open("mydata2.txt", encoding="utf-8")

except FileNotFoundError as ex:
    print("File not found.")
    print(ex.args)

else:
    print("File : ", myFile.read())
    myFile.close()

finally:
    print("Finished working with file")

