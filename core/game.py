import random
from core.dice import Dice
from core.board import Board

class game: 
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.board = Board()
        self.dice = Dice()