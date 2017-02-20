import unittest

from vector import Vector
from color import Color
from ray import Ray
from err import InvalidTypeError


class TestVector(unittest.TestCase):

    def test_default_init(self):
        v = Vector()
        self.assertEqual(v.x, 0)
        self.assertEqual(v.y, 0)
        self.assertEqual(v.z, 0)

    def test_equal(self):
        v = Vector()
        self.assertTrue(v.equal(Vector()))

    def test_equal_with_wrong_type(self):
        v = Vector()
        with self.assertRaises(InvalidTypeError):
            v.equal(4)


class TestColor(unittest.TestCase):

    def test_default_init(self):
        c = Color()
        self.assertEqual(c.r, 0)
        self.assertEqual(c.g, 0)
        self.assertEqual(c.b, 0)


class TestRay(unittest.TestCase):

    def test_default_init(self):
        ray = Ray()
        self.assertTrue(ray.origin.equal(Vector()))
        self.assertTrue(ray.dir.equal(Vector()))

if __name__ == '__main__':
    unittest.main()
