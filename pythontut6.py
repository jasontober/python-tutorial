# lists, bubble sort and list comprehensions
import random
import math
"""
# [0 : "string"] [1 : 1.234] [2 : 28] [3 : "c"]

randList = ["string", 1.234, 28]

oneToTen = list(range(10))

randList = randList + oneToTen

print(randList[0])

print("List length : ", len(randList))

first3 = randList[:3]

for i in first3:
    print("{} : {}".format(first3.index(i), i))

print(first3[0] * 3)

print("string" in first3)

print("Index of string : ", first3.index("string"))

print("How many strings : ", first3.count("string"))

first3[0] = "New String"

first3.append("Another")

for i in first3:
    print("{} : {}".format(first3.index(i), i))
"""
"""
# generate a random list
# list 5 numbers between 1 and 9

randList = []
num = 0

for i in range(5):
    while True:
        num = random.randrange(10)
        if not (num in randList):
            randList.append(num)
            break

for i in randList:
    print("{} : {}".format(randList.index(i), i))
"""
"""
# Bubblesort
# 1. An outer loop decreases in size each time
# 2. the goal is to have the largest number at the end of
#  the list when the outer loop completes 1 cycle
# 3. the inner loop starts comparing indexes at the beginning of the loop
# 4. check if list[index] > list[index + 1]
# 5. if so, swap the index values
# 6. When the inner loop completes the largest number is at the end of the list
# 7 decrement the outer loop by 1

numList = []
num = 0

for i in range(5):
    while True:
        num = random.randrange(10)
        if not (num in numList):
            numList.append(num)
            break

# for i in numList:
#    print(i, end=", ")

i = len(numList) - 1

while i >= 1:
    j = 0
    while j < i:
        print("\nIs {} > {}".format(numList[j], numList[j + 1]))
        if numList[j] > numList[j + 1]:
            print("Switch")
            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp
        else:
            print("Don't Switch")
        j += 1
        for k in numList:
            print(k, end=", ")
        print()
    print("END OF ROUND")
    i -= 1

for k in numList:
    print(k, end=", ")
print()
"""
"""
numList = []
num = 0

for i in range(5):
    while True:
        num = random.randrange(10)
        if not (num in numList):
            numList.append(num)
            break

numList.sort()

numList.reverse()

numList.insert(5, 10)

numList.remove(10)

numList.pop(2)

for i in numList:
    print(i, end=", ")
"""

# list comprehensions
"""
evenList = [i*2 for i in range(10)]

for i in evenList:
    print(i)

numList = [1,2,3,4,5]

listOfValues = [[math.pow(m,2), math.pow(m,3), math.pow(m,4)]
                for m in numList]

for i in listOfValues:
    print(i)
print()


multiDList = [[0] * 10 for i in range(10)]

multiDList[0][1] = 10

for i in multiDList:
    print(i)
print()

listTable = [[0] * 10 for i in range(10)]

for i in range(10):
    for j in range(10):
        listTable[i][j] = "{} : {}".format(i, j)

for i in range(10):
    for j in range(10):
        print(listTable[i][j], end=" || ")
    print()

"""
# create a multiplication table
while True:
    try:
        size = int(input("Please enter size of multiplication table : "))
        break
    except ValueError:
        print("Invalid valid value entered!")
    except:
        print("Unknown error.")

listTable = [[0] * size for i in range(size)]

for i in range(1, size):
    for j in range(1, size):
        listTable[i][j] = i * j

for i in range(1, size):
    for j in range(1, size):
        print(listTable[i][j], end="\t")
    print()
