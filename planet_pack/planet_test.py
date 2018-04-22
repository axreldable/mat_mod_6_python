import unittest

from planet_pack.planet import *


class TestStringMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Point(1, 2).add(Point(3, 4)), Point(4, 6))

    def test_minus(self):
        self.assertEqual(Point(1, 2).minus(Point(3, 4)), Point(-2, -2))

    def test_multi(self):
        self.assertEqual(Point(1, 2).multi(2), Point(2, 4))

    def test_distance(self):
        self.assertEqual(distance(Point(0, 0), Point(2, 0)), 8.0)

    def test_f(self):
        self.assertEqual(get_f(Point(0, 0), Point(2, 0)), Point(0.25, 0))

    def test_print(self):
        x, y = get_coordinates_array([Point(1, 1), Point(3, 50), Point(10, 25)])
        self.assertEqual(x, [1, 3, 10])
        self.assertEqual(y, [1, 50, 25])


if __name__ == '__main__':
    unittest.main()