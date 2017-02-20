# from geometric_object import GeometricObject
from vector import Vector
from ray import Ray

HIT_ERR = 0.0001


class Plane(object):

    def __init__(self, pos, normal):
        self.pos = Vector()
        self.pos.set(pos)

        self.normal = Vector()
        self.normal.set(normal)

    def hit(self, ray):
        t = self.normal * (self.pos - ray.origin) / (self.normal * ray.dir)

        if(t > HIT_ERR):
            print(t)
            return {'hit': True, 'tmin': t}

        return {'hit': False}
