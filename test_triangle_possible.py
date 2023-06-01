import unittest
from triangle_possible import triangle_possible


class TestTrianglePossible(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(triangle_possible(35, 90, 55), "Triangle possible with the given angles!")

    def test_negative(self):
        self.assertEqual(triangle_possible(47, 55, 151), "Triangle not possible with the given angles!")


if __name__ == '__main__':
    unittest.main()
