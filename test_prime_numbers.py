import unittest
from prime_numbers import prime_numbers


# variables
a = 1
b = 2


# unittest documentation at 
# https://docs.python.org/3/library/unittest.html#module-unittest
class TestPrimeNumbers(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertEqual(function(1, 1), 2)


if __name__ == '__main__':
    unittest.main()
