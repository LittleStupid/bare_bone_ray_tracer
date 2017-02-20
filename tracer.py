# from world import World
from color import Color


class SphereTracer(object):

    def __init__(self, world):
        self.world = world

    def trace_ray(self, ray):
        result = self.world.sphere.hit(ray)
        if result['hit'] == True:
            red = Color()
            red.r = 200
            return red

        return Color()
