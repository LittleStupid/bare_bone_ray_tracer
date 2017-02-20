# from world import World
from color import Color


class SphereTracer(object):

    def __init__(self, world):
        self.world = world

    def trace_ray(self, ray):
        result = self.world.sphere.hit(ray)
        if result['hit'] == True:
            return self.world.sphere.color

        return Color()


class SpheresTracer(object):

    def __init__(self, world):
        self.world = world

    def trace_ray(self, ray):
        tmin = 9999999
        color = Color()
        for sphere in self.world.spheres:
            result = sphere.hit(ray)
            if(result['hit'] == True):
                if(result['tmin'] < tmin):
                    color = sphere.color
        return color
