import unittest
from core.dice import Dice

class TestDice(unittest.TestCase):

    def test_roll_generates_two_values(self):
        dice = Dice()
        values = dice.roll()
        # Puede ser 2 normales o 4 si es doble
        self.assertTrue(len(values) in (2, 4))
        for v in values:
            self.assertTrue(1 <= v <= 6)

    def test_get_values_matches_last_roll(self):
        dice = Dice()
        rolled = dice.roll()
        values = dice.get_values()
        self.assertEqual(values, rolled)

if __name__ == '__main__':
    unittest.main()
