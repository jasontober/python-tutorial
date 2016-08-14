# reading/writing files, tuples and recursive functions
"""
import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:     # a for append
    myFile.write("some random text\nMore random text\nand some more")

with open("mydata.txt", encoding="utf-8") as myFile:
    print(myFile.read())

print(myFile.closed)

print(myFile.name)

print(myFile.mode)

os.rename("mydata.txt", "mydata2.txt")

os.remove("mydata2.txt")

# os.mkdir("myDir")

os.chdir("myDir")

print("Current Directory : ", os.getcwd())

os.chdir("..")

print("Current Directory : ", os.getcwd())

os.rmdir("myDir")

"""
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

# prompt user for quantity of fibonacci numbers to print out
while True:
    try:
        fibQuant = int(input("Please enter the quantity of Fibonacci numbers to print : "))
        break
    except ValueError:
        print("Not a valid entry.")
    except:
        print("Unknown Error!")

# print Fibonacci numbers to console
for i in range(fibQuant):
    print(fibonacci(i), end=" ")
"""
"""
import os

with open("mydata2.txt", mode="w", encoding="utf-8") as myFile:     # a for append
    myFile.write("some random text\nMore random text\nand some more")

with open("mydata2.txt", encoding="utf-8") as myFile:
    lineNum = 1

    while True:
        line = myFile.readline()

        if not line:
            break

        # split string into list
        wordsList = line.split()
        # print("wordList : ", wordsList)
        # calculate how many words on current line
        wordCount = len(wordsList)
        # print("Word Count = ", wordCount)
        # calculate average word length of words on current line
        sum = 0
        for word in wordsList:
            sum += len(word)
            # print("Sum = ", sum)
        wordLen = sum / wordCount
        # print("Average Word Length = ", wordLen)

        # print to console
        print("Line{} : {}\twords = {}\tav.length = {:.2f}".format(lineNum, line, wordCount, wordLen))
        lineNum += 1
"""

# tuples like lists, but cannot be changed

myTuple = (1, 2, 3, 5, 8)

print("1st Value", myTuple[0])

print(myTuple[0:3])

print("Tuple length = ", len(myTuple))

moreFibs = myTuple + (13, 21, 34)

print("32 in Tuple : ", 32 in moreFibs)

for i in moreFibs:
    print(i)

aList = [55, 89, 144]

aTuple = tuple(aList)

aList = list(aTuple)

print("Min = ", min(aTuple))
print("Max = ", max(aTuple))