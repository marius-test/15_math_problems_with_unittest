import unittest
from sum_of_cubes import sum_of_cubes


class TestSumOfCubes(unittest.TestCase):
    def test_sum_of_cubes(self):
        n = 6
        self.assertEqual(sum_of_cubes(n), 441)


if __name__ == '__main__':
    unittest.main()
