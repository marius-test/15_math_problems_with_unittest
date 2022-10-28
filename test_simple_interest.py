import unittest
from simple_interest import simple_interest


p = 2500
r = 3.5
t = 5


class TestSimpleInterest(unittest.TestCase):
    def test_simple_interest(self):
        self.assertEqual(simple_interest(p, r, t), 437.5)


if __name__ == '__main__':
    unittest.main()
