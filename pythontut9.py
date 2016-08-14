# Object Oriented Programming with Python
"""
Real world objects : Attributes & capabilities

Dog Attributes (fields/variables) : height, weight, favorite food

dog capabilities (methods/functions) : run, walk, eat
"""

"""
class Dog:

    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog barks".format(self.name))


def main():
    spot = Dog("Spot", 66, 26)

    spot.bark()

    bowser = Dog()

    bowser.bark()

main()
"""

"""
class Square:

    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retrieving the Height")

        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter numbers for height")

    @property
    def width(self):
        print("Retrieving the width")

        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")

    def get_area(self):
        return int(self.__width) * int(self.__width)


def main():
    aSquare = Square()

    height = input("Enter Height : ")
    width = input("Enter Width : ")

    aSquare.height = height
    aSquare.width = width

    print("Height :", aSquare.height)
    print("Width :", aSquare.width)
    print("Area is :", aSquare.get_area())

main()
"""

''' -- my solution
Each warrior has a sword and shield
they take turns attacking each other
the sword will inflict a random amount of damage,
the shield will block a random amount of damage
the difference is removed from the defenders health
The game continues until one warrior is victorious

Sam attacks Paul and deals 9 damage
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attacks Paul and deals 19 damage
Paul is down to -9 health
Paul has died and Sam is Victorious
Game Over

import random


# define class warrior
class Warrior:

    def __init__(self, name="", health=10, max_damage=10, max_block=10):
        self.name = name
        self.health = health
        self.max_damage = max_damage
        self.max_block = max_block

    @property
    def name(self):
        # print("Retrieving the name")
        return self.__name

    @name.setter
    def name(self, value):
        self.__name= value

    @property
    def health(self):
        # print("Retrieving the health")
        return self.__health

    @health.setter
    def health(self, value):
        self.__health= value

    def attack(self):
        return random.randrange(self.max_damage)

    def defend(self):
        return random.randrange(self.max_block)


def main():
    # create warriors
    warriorsList = []
    warriorsList.append(Warrior("Sam"))
    warriorsList.append(Warrior("Paul"))
    idx = 0

    # main game loop to be exited when one warrior has health that is <= 0
    while True:
        # check for invalid index value for the array
        if idx < 0 or idx > 1:
            print("Invalid idx value : ", idx)
            break

        # determine attacker and defender for printing to console
        if idx == 0:
            attacker = warriorsList[0].name
            attack = warriorsList[0].attack()
            defender = warriorsList[1].name
            defend = warriorsList[1].defend()
            health = warriorsList[1].health
        else:
            attacker = warriorsList[1].name
            attack = warriorsList[1].attack()
            defender = warriorsList[0].name
            defend = warriorsList[0].defend()
            health = warriorsList[0].health

        # determine attack and block values
        print("{} attacks for {} damage".format(attacker, attack))
        print("{} defends for {} damage".format(defender, defend))

        # determine if damage has been dealt and print to console
        damage = attack - defend
        if damage > 0:
            if idx == 0:
                warriorsList[1].health -= damage
            else:
                warriorsList[0].health -= damage
            health -= damage
            print("{} is damaged for {} damage".format(defender, abs(damage)))
        else:
            print("{} blocked the attack of {}!".format(defender, attacker))

        # monitor current defender's health
        print("{} is down to {} health".format(defender, health))

        # determine if game is over
        if health <= 0:
            print("{} has Died and {} is Victorious".format(defender, attacker))
            break
        else:
            # switch idx (0/1)
            if idx == 0:
                idx = 1
            else:
                idx = 0

        print("------------------------------------------------")

main()
'''

''' -- Banas solution
Sam attacks Paul and deals 9 damage
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attacks Paul and deals 19 damage
Paul is down to -9 health
Paul has died and Sam is Victorious
Game Over
'''

# Warrior and Battle Class
# Warriors wlll have names, health, and attack and block maximums
# Warriors will be able to attack and block random amounts


# Attack random() 0.0 - 1.0 * maxAttack + .5

# Block will use random() like attack

# Battle Class will loop until 1 warrior dies
# warriors will take turns to attack each other


# Function gets 2 warriors
# 1 warrior attacks the other
# attacks and blocks are integers


import random
import math


class Warrior:

    def __init__(self, name="Warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def attack(self):
        attkAmt = self.attkMax * (random.random() + .5)
        return attkAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)
        return blockAmt

class Battle:

    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break

            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):

        warriorAAttkAmt = warriorA.attack()

        warriorBBlockAmt = warriorB.block()

        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)
        if damage2WarriorB < 0:
            damage2WarriorB = 0

        warriorB.health = warriorB.health - damage2WarriorB

        print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, damage2WarriorB))

        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} has Died and {} is Victorious".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight Again!"


def main():
    maximus = Warrior("Maximus", 50, 20, 10)
    galaxon = Warrior("Galaxon", 50, 20, 10)
    battle = Battle()

    battle.startFight(maximus, galaxon)


main()
