import unittest
from core.rules import Rules

class TestRules(unittest.TestCase):

    def setUp(self):
        self.rules = Rules()
        
        self.board = [[] for _ in range(24)]
    
        self.board[0] = ["X"]
        self.board[5] = ["O", "O"]
        self.board[6] = ["X"]

    def test_valid_move(self):
        
        result = self.rules.is_valid_move(0, 6, 6, self.board)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
