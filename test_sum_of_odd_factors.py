import unittest
from sum_of_odd_factors import sum_odd_factors


class TestSumOddFactors(unittest.TestCase):
    def test_sum_odd_factors(self):
        self.assertEqual(sum_odd_factors(15), 24)
        self.assertEqual(sum_odd_factors(1), 1)
        self.assertEqual(sum_odd_factors(11), 12)


if __name__ == '__main__':
    unittest.main()
