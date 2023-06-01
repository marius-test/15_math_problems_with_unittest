import unittest
from cylinder_volume import cylinder_volume


class TestCylinderVolume(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(cylinder_volume(3, 6), "The volume of the cylinder is 169.65.")
        
    def test_negative(self):
        self.assertEqual(cylinder_volume(0, -9), "Please input positive numbers!")


if __name__ == '__main__':
    unittest.main()
