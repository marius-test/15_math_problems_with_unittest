import unittest
from fibonacci_number_check import fibonacci


class FibonacciNumberCheck(unittest.TestCase):
    def test_is_fibonacci(self):
        n = 1
        self.assertEqual(fibonacci(1), f"{n} is a Fibonacci number!")
        
    def test_is_not_fibonacci(self):
        n = 4
        self.assertEqual(fibonacci(4), f"{n} is not a Fibonacci number!")
    


if __name__ == '__main__':
    unittest.main()
