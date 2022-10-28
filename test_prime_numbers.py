import unittest
from prime_numbers import prime_numbers


class TestPrimeNumbers(unittest.TestCase):
    def test_prime_numbers(self):
        expected_list = [2, 3]
        self.assertEqual(prime_numbers(2, 3), expected_list)


if __name__ == '__main__':
    unittest.main()
