# importing is a way of using code from another python module than the current one
# a module is a python file
from largest_of_two_numbers import largest
import unittest

# variables
expected_message_for_equal_numbers = "The two numbers are equal"


# unittest documentation at https://docs.python.org/3/library/unittest.html#module-unittest
class TestLargest(unittest.TestCase):
    def test_a_is_larger(self):
        self.assertEqual(largest(95, 23), 95)

    def test_b_is_larger(self):
        self.assertEqual(largest(-65, 7), 7)
        
    def test_a_equals_b(self):
        self.assertAlmostEqual(largest(10, 10), expected_message_for_equal_numbers)


if __name__ == '__main__':
    unittest.main()
