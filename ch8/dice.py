from random import randint

class Dice:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__size = 30
        self.__value = 1

    def read_dice(self):
        return self.__value

    def print_dice(self):
        print("주사위의 값=",self.__value)

    def roll_dice(self):
        self.__value = randint(1,6)

d = Dice(100,100)
d. roll_dice()
d.print_dice()