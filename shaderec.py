from vector import Vector
from color import Color


class ShadeRec(object):

    def __init__(self):
        self.hit = False
        self.hit_location = Vector()
        self.normal = Vector()
        self.color = Color()
