from err import InvalidTypeError
import math


def dot(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z


def scale(a, scale):
    result = Vector()

    result.x = a.x * scale
    result.y = a.y * scale
    result.z = a.z * scale

    return result


class Vector(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def __str__(self):
        return 'Vector: %s, %s, %s' % (self.x, self.y, self.z)

    def __add__(self, that):
        result = Vector()

        result.x = self.x + that.x
        result.y = self.y + that.y
        result.z = self.z + that.z

        return result

    def __sub__(self, that):
        result = Vector()

        result.x = self.x - that.x
        result.y = self.y - that.y
        result.z = self.z - that.z

        return result

    def __mul__(self, that):
        if isinstance(that, Vector):
            return dot(self, that)

        if isinstance(that, (int, float)):
            return scale(self, that)

        raise(InvalidTypeError('Invalid type error: %s' % type(that)))

    def equal(self, that):
        if that is None:
            return False

        if False == isinstance(that, Vector):
            raise(InvalidTypeError('Invalid type error: %s' % type(that)))

        if self.x != that.x:
            return False

        if self.y != that.y:
            return False

        if self.z != that.z:
            return False

        return True

    def set(self, that):
        if False == isinstance(that, Vector):
            raise(InvalidTypeError('Invalid type error: %s' % type(that)))

        self.x = that.x
        self.y = that.y
        self.z = that.z

    def normalize(self):
        length_sq = self * self
        length = math.sqrt(length_sq)

        self.x = self.x / length
        self.y = self.y / length
        self.z = self.z / length

    def cross(self, that):
        x = self.y * that.z - self.z * that.y
        y = self.z * that.x - self.x * that.z
        z = self.x * that.y - self.y * that.x

        v = Vector()
        v.x = x
        v.y = y
        v.z = z

        return v
