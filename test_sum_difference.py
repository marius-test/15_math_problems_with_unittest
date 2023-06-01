import unittest
from sum_difference import sum_difference


class TestSumDifference(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(sum_difference(1), 0)
        self.assertEqual(sum_difference(3), 22)

    def test_big_numbers(self):
        self.assertEqual(sum_difference(12), 5434)
        self.assertEqual(sum_difference(94), 19654930)


if __name__ == '__main__':
    unittest.main()
