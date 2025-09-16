import unittest
from core.rules import Rules

class TestRules(unittest.TestCase):

    def setUp(self):
        self.rules = Rules()
        # tablero con 24 puntos, cada punto es una lista
        self.board = [[] for _ in range(24)]

        self.board[0] = ["X"]
        self.board[5] = ["O", "O"]
        self.board[6] = ["X"]

    def test_valid_move(self):
        # mover ficha de 0 a 6 con dado 6
        result = self.rules.is_valid_move(0, 6, 6, self.board)
        self.assertTrue(result)

    def test_invalid_empty_start(self):
        # intentar mover de un punto vacío
        result = self.rules.is_valid_move(3, 5, 2, self.board)
        self.assertFalse(result)

    def test_invalid_blocked_point(self):
        # intentar mover a un punto bloqueado (más de 1 ficha del oponente)
        result = self.rules.is_valid_move(0, 5, 5, self.board)
        result = self.rules.is_valid_move(6, 5, 1, self.board)
        self.assertFalse(result)

    def test_invalid_wrong_dice(self):
        
        result = self.rules.is_valid_move(0, 5, 3, self.board)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
