import unittest
from sum_of_array import sum_of_array


class TestSumOfArray(unittest.TestCase):
    def test_a(self):
        array1 = [2, 5, 9]
        self.assertEqual(sum_of_array(array1), 16)


if __name__ == '__main__':
    unittest.main()
