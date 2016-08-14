# inheritance, polymorphism, magic methods
"""
class Animal:

    def __init__(self, birthType="Unknown",
                 appearance="Unknown", blooded="Unknown"):
        self.birthType = birthType
        self.appearance = appearance
        self.blooded = blooded

    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    def __str__(self):
        return "A {} is {} it has {} it is {}".format(type(self).__name__, self.birthType, self.appearance, self.blooded)


class Mammal(Animal):

    def __init__(self, birthType="born live",
                 appearance="hair or fur",
                 blooded="warm-blooded",
                 nurseYoung=True):
        Animal.__init__(self, birthType, appearance, blooded)
        self.__nurseYoung = nurseYoung

    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    def __str__(self):
        return super().__str__() + " and it is {} they nurse their young".format(self.nurseYoung)


class Reptile(Animal):

    def __init__(self, birthType="born in an egg or born alive",
                 appearance="dry scales",
                 blooded="cold-blooded"):
        Animal.__init__(self, birthType, appearance, blooded)

    def sumAll(self, *args):
        sum = 0

        for i in args:
            sum += i

        return sum


def getBirthType(theObject):
    print("The {} is {}".format(type(theObject).__name__,
                                theObject.birthType))

def main():
    animal1 = Animal("born alive")

    print(animal1.birthType)

    print(animal1)
    print()

    mammal1 = Mammal()

    print(mammal1.birthType)
    print(mammal1.appearance)
    print(mammal1.blooded)
    print(mammal1.nurseYoung)

    print(mammal1)
    print()

    reptile1 = Reptile()

    print(reptile1.birthType)
    print(reptile1.appearance)
    print(reptile1.blooded)

    print(reptile1)
    print()

    print("Sum : {}".format(reptile1.sumAll(1,2,3,4,5,6,3,3,2,9)))

    getBirthType(mammal1)
    getBirthType(reptile1)


main()
"""

# magic methods
# __eq__ : Equal
# __ne__ : Not Equal
# __lt__ : less than
# __gt__ : greater than
# __le__ : less than or equal to
# __ge__ : greater than or equal to
# __add__ : add
# __sub__ : subtract
# __mul__ : multiply
# __div__ : divide
# __mod__ : Modulus
# __str__ : string

class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def __add__(self, other_time):
        newTime = Time()

        newTime.second = self.second + other_time.second
        while newTime.second >= 60:
            newTime.minute += 1
            newTime.second -= 60

        newTime.minute += self.minute + other_time.minute
        while newTime.minute >= 60:
            newTime.hour += 1
            newTime.minute -= 60

        newTime.hour += self.hour + other_time.hour
        while newTime.hour >= 24:
            newTime.hour -= 24

        return newTime

def main():

    time1 = Time(10,45,22)
    time2 = Time(15,30,50)

    print(time1)
    print(time2)

    print(time1 + time2)

main()







