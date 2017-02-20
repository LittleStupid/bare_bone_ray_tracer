from vector import Vector
from color import Color
import math

SPHERE_ERR = 0.0001


class Sphere(object):

    def __init__(self, pos, r):
        self.pos = Vector()
        self.pos.set(pos)
        self.r = r

        self.color = Color()
        self.color.r = 200

    def hit(self, ray):
        center_diff = ray.origin - self.pos

        a = ray.dir * ray.dir
        b = 2 * (ray.dir * center_diff)
        c = center_diff * center_diff - self.r * self.r
        delta = b * b - 4 * (a * c)

        if delta < 0:
            return {'hit': False}

        e = math.sqrt(delta)

        t = (-b - e) / (2 * a)
        if(t > SPHERE_ERR):
            return {'hit': True, 'tmin': t}

        t = (-b + e) / (2 * a)
        if(t > SPHERE_ERR):
            return {'hit': True, 'tmin': t}

        return {'hit': False}
