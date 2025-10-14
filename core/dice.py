import random
class Dice:
    def __init__(self):
        self.__values__ = []

    def roll(self):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        self.__values__ = [d1, d2]
        return self.__values__  if d1 != d2 else [d1]*4
             
    def get_values(self):
        return self.__values__