import pytest
from core.dice import Dice

def test_roll_generates_two_values():
    dice = Dice()
    values = dice.roll()

    assert len(values) == 2

    assert all(1 <= v <= 6 for v in values)

def test_get_values_matches_last_roll():
    dice = Dice()
    rolled = dice.roll()
    values = dice.get_values()

    assert rolled == values

if __name__ == '__main__':
    unittest.main()