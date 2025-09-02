import unittest
from core.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_board_has_24_points(self):
        points = self.board.get_points()
        self.assertEqual(len(points), 24)

    def test_initial_setup_correct(self):
        points = self.board.get_points()

        self.assertEqual(len(points[0]), 2)   # Punto 1 con 2 fichas
        self.assertEqual(len(points[11]), 5)  # Punto 12 con 5 fichas
        self.assertEqual(len(points[16]), 3)  # Punto 17 con 3 fichas
        self.assertEqual(len(points[18]), 5)  # Punto 19 con 5 fichas

    def test_other_points_empty(self):
        points = self.board.get_points()
        empty_points = [i for i, p in enumerate(points) if len(p) == 0]

        expected_empty = [i for i in range(24) if i not in [0, 11, 16, 18]]
        self.assertEqual(empty_points, expected_empty)


if __name__ == '__main__':
    unittest.main()
