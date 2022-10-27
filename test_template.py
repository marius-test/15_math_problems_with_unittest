import unittest
from template import function


# variables
a = 1
b = 2


# unittest documentation at https://docs.python.org/3/library/unittest.html#module-unittest
class TestName(unittest.TestCase):
    def test_a(self):
        self.assertEqual(function(1, 1), 2)

    def test_b(self):
        self.assertEqual(function(1, 2), 3)
        
    def test_c(self):
        self.assertEqual(function(1, -1), 0)


if __name__ == '__main__':
    unittest.main()
