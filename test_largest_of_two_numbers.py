from largest_of_two_numbers import largest
import unittest


class TestLargest(unittest.TestCase):
    def test_a_is_larger(self):
        self.assertEqual(largest(95, 23), 95)

    def test_b_is_larger(self):
        self.assertEqual(largest(-65, 7), 7)
        
    def test_a_equals_b(self):
        self.assertEqual(largest(10, 10), "The numbers are equal")


if __name__ == '__main__':
    unittest.main()
