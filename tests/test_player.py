import unittest
from core.player import Player

class TestPlayer(unittest.TestCase):

    def test_init_player(self):
        p = Player("Juan", "X")
        self.assertEqual(p.get_name(), "Juan")
        self.assertEqual(p.get_color(), "X")
        self.assertEqual(p.get_checkers(), 15)

    def test_remove_checker(self):
        p = Player("Ana", "O")
        p.remove_checker()
        self.assertEqual(p.get_checkers(), 14)

    def test_add_checker(self):
        p = Player("Luis", "X")
        p.add_checker()
        self.assertEqual(p.get_checkers(), 16)

if __name__ == "__main__":
    unittest.main()