import random
class Dice:
    def __init__(self):
        self.__values__ = []

    def roll(self):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)


