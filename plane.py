# from geometric_object import GeometricObject
from vector import Vector
from ray import Ray


class Plane(GeometricObject):

    def __init__(self, pos, normal):
        self.pos = Vector()
        self.pos.set(pos)

        self.normal = Vector()
        self.normal.set(normal)

    def hit(self, ray):
        pass

    def getSmallErr(self):
        return 0.0001
