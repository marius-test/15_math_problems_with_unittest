import unittest
from nth_fibonacci_number import nth_fibonacci_number


class TestNthFibonacci(unittest.TestCase):
    def test_a(self):
        self.assertEqual(nth_fibonacci_number(7), 13)


if __name__ == '__main__':
    unittest.main()
    