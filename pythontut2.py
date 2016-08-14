# looping

"""
# print odds 1 to 20 use a for loop, range, modulus

#create for loop from 1-20
for i in range(1, 21):
    if not((i%2)==0):
        print("i =", i)

"""

"""
your_float = input("Enter a float:")

your_convert = float(your_float)

print("Rounded to 2 decimals : {:.2f}".format(your_convert))
"""

"""
# demonstrate compound interest
# Have user enter their investment amount and expected interest
# each year their investment wil increase by their investment + their investment * interest
# print out earnings after 10 years

# ask user for investment and interest rate
inpInvest = input("Enter your initial investment: ")
inpRate = input("Enter your interest rate:")

# convert to float
fInvest = float(inpInvest)
fRate = float(inpRate)
if (fRate >= 1.0): fRate = float(inpRate) * .01

# calculate earnings
for i in range(10):
    fInvest = fInvest + (fInvest * fRate)

# print outcome
print("Your earnings after 10 years = {:.2f}".format(fInvest))
"""
"""
import random
rand_num = random.randrange(1,51)

i = 1

while (i <= 20):
    if ((i % 2) == 0):
        i += 1
        continue

    if (i == 15):
        break

    print("Odd : ", i)

    i += 1

#print ("The random value is : ", rand_num)
"""


""" - my solution
Ask user for height of tree
How tall is he tree? 5
    #
   ###
  #####
 #######
#########
    #


0  |---------#---------     9   1   9   19
1  |--------###--------     8   3   8   19
2  |-------#####-------     7   5   7   19
3  |------#######------     6   7   6   19
4  |-----#########-----     5   9   5   19
5  |----###########----     4   11  4   19
6  |---#############---     3   13  3   19
7  |--###############--     2   15  2   19
8  |-#################-     1   17  1   19
9  |###################     0   19  0   19
10 |---------#---------     9   1   9   19


use 1 while loop and 3 for loops
should handle any height of tree


# Ask user for height of tree5

treeHeight = eval(input("How tall is the tree?"))

# initialize values
loop = 0
lineString = ''
firstString = ''

# create while loop
while (loop<=treeHeight):

    if (loop == treeHeight):
        print(firstString)
        break
    # create ' ' loop
    for i in range(treeHeight-loop-1):
        lineString = lineString + ' '

    # create '#' loop
    for i in range((loop*2)+1):
        lineString = lineString + '#'

    # print to console
    print(lineString)

    # simplify first-last row congruity
    if (loop == 0):
        firstString = lineString

    # reinitialize
    lineString = ''

    # increment counter
    loop += 1
"""

''' -- Banas solution
Ask user for height of tree
How tall is he tree? 5
    #
   ###
  #####
 #######
#########
    #

# use 1 while loop and 3 for loops
# 4 spaces : 1 hash
# 3 spaces : 3 hashes
# 2 spaces : 5 hashes
# 1 spaces : 7 hashes
# 0 spaces : 9 hashes

# Need to do
# 1. decrement spaces by 1 each time through the loop
# 2. increment the hashes by 2 each time through the loop
# 3. save spaces to the stump by calculating tree height - 1
# 4. decrement from tree height until it equals 0
# 5. print spaces and then hashes for each row
# 6. print stump spaces and then 1 hash

# Get the number of rows for the tree
treeHeight = input("How tall is the tree?")
# Convert into integer
treeHeight = int(treeHeight)
# get the starting spaces for top of the tree
spaces = treeHeight - 1
# There is 1 hash to start that will be incremented
hashes = 1
# save stump spaces until later
stumpSpaces = spaces
# make sure the right number of rows are printed
while treeHeight > 0:
# print the spaces
# end = ""
    for i in range(spaces):
        print(' ', end="")

# print the hashes
    for i in range(hashes):
        print('#', end="")

# newline after each row is printed
    print()
# spaces is decremented by 1
    spaces -= 1
# hashes will be incremented by 2
    hashes += 2
# decrement tree height each time
    treeHeight -= 1
# print the spaces before the stump
for i in range(stumpSpaces):
    print(' ', end="")

print('#')
'''

