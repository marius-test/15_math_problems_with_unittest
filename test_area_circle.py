import unittest
from circle_area import circle_area


class CircleArea(unittest.TestCase):
    def test_circle_area(self):
        self.assertEqual(circle_area(10), 314.16)


if __name__ == '__main__':
    unittest.main()
