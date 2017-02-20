import unittest

from vector import Vector
from color import Color
from ray import Ray
from plane import Plane
from sphere import Sphere
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

    def test_set_vector(self):
        v = Vector()

        that = Vector()
        that.x = 1.1
        that.y = 2.2

        v.set(that)

        self.assertEqual(v.x, that.x)
        self.assertEqual(v.y, that.y)
        self.assertEqual(v.z, that.z)

        self.assertEqual(v.x, 1.1)
        self.assertEqual(v.y, 2.2)
        self.assertEqual(v.z, 0.0)

        self.assertTrue(v.equal(that))

    def test_add(self):
        v1 = Vector()
        v1.x = 1
        v1.y = 3

        v2 = Vector()
        v2.x = 8
        v2.y = 9

        v3 = v1 + v2
        self.assertEqual(v3.x, 9)
        self.assertEqual(v3.y, 12)
        self.assertEqual(v3.z, 0)

    def test_sub(self):
        v1 = Vector()
        v1.x = 100
        v1.y = 50
        v1.z = 20

        v2 = Vector()
        v2.x = 9
        v2.y = 9
        v2.z = 9

        v3 = v1 - v2
        self.assertEqual(v3.x, 91)
        self.assertEqual(v3.y, 41)
        self.assertEqual(v3.z, 11)

    def test_dot(self):
        v1 = Vector()
        v1.x = 100
        v1.y = 50
        v1.z = 20

        v2 = Vector()
        v2.x = 9
        v2.y = 9
        v2.z = 9

        r = v1 * v2
        self.assertEqual(r, 900 + 450 + 180)

    def test_scale(self):
        v1 = Vector()
        v1.x = 100
        v1.y = 50
        v1.z = 20

        scale = 2
        v3 = v1 * scale
        self.assertEqual(v3.x, 200)
        self.assertEqual(v3.y, 100)
        self.assertEqual(v3.z, 40)


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

    def test_set_dir_vector(self):
        ray = Ray()

        v = Vector()
        v.x = 1
        v.y = 2
        v.z = 3

        ray.setDir(v)
        self.assertTrue(ray.dir.equal(v))

    def test_set_dir_xyz(self):
        ray = Ray()

        v = Vector()
        v.x = 1
        v.y = 2
        v.z = 3

        ray.setDirXYZ(1, 2, 3)
        self.assertTrue(ray.dir.equal(v))

    def test_set_origin_vector(self):
        ray = Ray()

        v = Vector()
        v.x = 1
        v.y = 2
        v.z = 3

        ray.setOrigin(v)
        self.assertTrue(ray.origin.equal(v))

    def test_set_origin_xyz(self):
        ray = Ray()

        v = Vector()
        v.x = 1
        v.y = 2
        v.z = 3

        ray.setOriginXYZ(1, 2, 3)
        self.assertTrue(ray.origin.equal(v))

    def test_plane_hit(self):
        ray = Ray()
        ray.setOriginXYZ(10, 10, 10)
        ray.setDirXYZ(0, 0, -1)

        pos = Vector()
        normal = Vector()
        normal.z = 1
        plane = Plane(pos, normal)

        result = plane.hit(ray)

        self.assertEqual(result['hit'], True)
        self.assertEqual(result['tmin'], 10)

    def test_sphere_hit(self):
        ray = Ray()
        ray.setOriginXYZ(0, 0, 10)
        ray.setDirXYZ(0, 0, -1)

        pos = Vector()
        pos.x = pos.y = pos.z = 0
        r = 1
        sphere = Sphere(pos, r)

        result = sphere.hit(ray)
        self.assertEqual(result['hit'], True)
        self.assertEqual(result['tmin'], 9)

    def test_print_vector(self):
        v = Vector()
        v.x = 1
        v.y = 2
        v.z = 3

        self.assertEqual(v.__str__(), 'Vector: 1, 2, 3')

if __name__ == '__main__':
    unittest.main()
