import unittest
from sum_of_squares import sum_of_squares


class TestSumOfSquares(unittest.TestCase):
    def test_sum_of_squares(self):
        n = 5
        self.assertEqual(sum_of_squares(n), 55)


if __name__ == '__main__':
    unittest.main()
