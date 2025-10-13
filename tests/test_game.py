import unittest
from core.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game("Gino", "Pablo")

    def test_initial_turn(self):
        # Al inicio el turno es del jugador 1
        self.assertEqual(self.game.get_turn(), "Gino")

    def test_switch_turn(self):
        self.game.switch_turn()
        self.assertEqual(self.game.get_turn(), "Pablo")
        self.game.switch_turn()
        self.assertEqual(self.game.get_turn(), "Gino")

    def test_roll_dice_returns_values(self):
        values = self.game.roll_dice()
        self.assertTrue(len(values) in (2, 4))  # 2 normales o 4 si es doble
        for v in values:
            self.assertTrue(1 <= v <= 6)

if __name__ == "__main__":
    unittest.main()
