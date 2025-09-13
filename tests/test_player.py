import unittest
from core.player import Player

class TestPlayer(unittest.TestCase):

    def test_init_player(self):
        p = Player("Juan", "X")
        self.assertEqual(p.get_name(), "Juan")
        self.assertEqual(p.get_color(), "X")
        self.assertEqual(p.get_checkers(), 15)