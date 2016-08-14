# String functions
'''
rand_string = "      this is an important string      "

rand_string = rand_string.lstrip()
rand_string = rand_string.rstrip()
rand_string = rand_string.strip()

print(rand_string.capitalize())
print(rand_string.upper())
print(rand_string.lower())

a_list = ["bunch","of","random","words"]
print(" ".join(a_list))

a_list2 = rand_string.split()
for i in a_list2:
    print(i)

print("How many is = ", rand_string.count("is"))

print("Where is string : ", rand_string.find("string"))

print(rand_string.replace("an ", "a kind of "))

'''
'''- my solution
# Acronym generator
# Random Access Memory : RAM
# user enters string, convert string into an acronym in upper case

# prompt user for phrase
inp_user = input("Please enter a phrase : ")

# parse input into list
a_list = inp_user.split()

# generate Acronym
acro_string = ''
for i in a_list:
    acro_string += i[0].upper()
# print to console

print(inp_user + " : " + acro_string)

'''

'''- tutorial solution
# Acronym generator
# Random Access Memory : RAM
# user enters string, convert string into an acronym in upper case

# Ask for a string
inp_user = input("Please enter a phrase : ")
print(inp_user + " : ", end="")

# Convert the string to uppercase
inp_user = inp_user.upper()

# convert the string to a list
a_list = inp_user.split()

# cycle through the list
for i in a_list:
    # get the first letter of the word and eliminate the newline
    print(i[0], end="")

# add a newline
print()
'''

'''
letter_z = "z"
num_3 = "3"
a_space = " "

print("Is z a letter or number : ", letter_z.isalnum())
print("Is z a letter : ", letter_z.isalpha())
print("Is 3 a number : ", num_3.isdigit())
print("Is z a lowercase : ", letter_z.islower())
print("Is z a uppercase : ", letter_z.isupper())
print("Is space a space : ", a_space.isspace())
'''
'''
def isfloat(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False

print("is PI a float :", isfloat(num_3))
'''

# implement Caesar's cypher
'''
A -> D
B -> E
A-Z 65-90
a-z 97-122
ord(your_letter)
chr(your_code)
'''
# check if char is letter, if not leave as is
# Hints
# Use isupper() to decide which unicodes to work with
# add the key (number of characters to shift) and if
# the key is bigger or smaller than the unicode for
# A, Z, a, z increase or decrease by 26


def encrypt(message, key):
    return_message = ""
    for char in message:
        # check if character is letter or symbol
        if char.isalpha():
            coded_char = ord(char) + key
            # check if using upper or lower case letter
            if char.isupper():
                if (coded_char < ord("A")):
                    coded_char += 26
                elif (coded_char > ord("Z")):
                    coded_char -= 26
            else:
                if (coded_char < ord("a")):
                    coded_char += 26
                elif (coded_char > ord("z")):
                    coded_char -= 26
            return_message += chr(coded_char)
        else:
            return_message += chr(ord(char))

    # return string
    return return_message

# prompt user for phrase to be encoded
phrase = input("Please enter phrase to be encoded : ")

# prompt user for key
while True:
    try:
        key = int(input("Please enter key for cypher :"))
        break
    except ValueError:
        print("not a valid number.")
    except:
        print("unknown error")

# cycle through characters
'''
encoded_message = ''
for char in phrase:
    # check if character is letter or symbol
    if char.isalpha():
        coded_char = ord(char) + key
        # check if using upper or lower case letter
        if char.isupper():
            if (coded_char < ord("A")):
                coded_char += 26
            elif (coded_char > ord("Z")):
                coded_char -= 26
        else:
            if (coded_char < ord("a")):
                coded_char += 26
            elif (coded_char > ord("z")):
                coded_char -= 26
        encoded_message += chr(coded_char)
    else:
        encoded_message += chr(ord(char))
'''
# print out code
encoded_message = encrypt(phrase, key)
print("Coded message : ", encoded_message)

key = -key
'''
orig_message = ""
for char in encoded_message:
    # check if character is letter or symbol
    if char.isalpha():
        coded_char = ord(char) + key
        # check if using upper or lower case letter
        if char.isupper():
            if (coded_char < ord("A")):
                coded_char += 26
            elif (coded_char > ord("Z")):
                coded_char -= 26
        else:
            if (coded_char < ord("a")):
                coded_char += 26
            elif (coded_char > ord("z")):
                coded_char -= 26
        orig_message += chr(coded_char)
    else:
        orig_message += chr(ord(char))
'''
# print out code
orig_message = encrypt(encoded_message, key)
print("Decoded message : ", orig_message)

