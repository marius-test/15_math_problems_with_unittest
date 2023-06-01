import unittest
from sum_of_divisors import sum_divisors


class TestSumDivisors(unittest.TestCase):
    def test_prime_number(self):
        self.assertEqual(sum_divisors(3), 1)

    def test_composite_number(self):
        self.assertEqual(sum_divisors(18), 21)


if __name__ == '__main__':
    unittest.main()
