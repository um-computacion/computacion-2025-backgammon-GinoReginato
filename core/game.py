import random
from core.dice import Dice
from core.board import Board

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.__board__ = Board()
        self.dice = Dice()
        self.remaining_dice = []

    def get_turn(self):
        return self.current_player

    def switch_turn(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        self.remaining_dice = []

    def roll_dice(self):
        values = self.dice.roll()
        if len(values) == 2 and values[0] == values[1]:
            values *= 2
        self.remaining_dice = values.copy()
        return values

    def use_die(self, distance):
        if distance in self.remaining_dice:
            self.remaining_dice.remove(distance)
            if not self.remaining_dice:
                self.switch_turn()
            return True
        return False



