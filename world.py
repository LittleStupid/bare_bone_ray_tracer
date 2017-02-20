from view_plane import ViewPlane
from sphere import Sphere
from vector import Vector
from tracer import SphereTracer, SpheresTracer
from ray import Ray
from PIL import Image, ImageDraw
import time


class World(object):

    def __init__(self):
        self.vp = ViewPlane()

        pos = Vector()
        pos.x = 0
        pos.y = 300
        pos.z = -20
        self.sphere = Sphere(pos, 200)

        self.tracer = SphereTracer(self)
        self.mul_tracer = SpheresTracer(self)

        self.spheres = []

        pos1 = Vector()
        pos1.x = 0
        pos1.y = 100
        self.spheres.append(Sphere(pos1, 125))

        pos2 = Vector()
        pos2.x = 50
        pos2.y = 150
        self.spheres.append(Sphere(pos2, 120))

        self.spheres[0].color.g = 200
        self.spheres[0].color.b = 200
        self.spheres[1].color.b = 200

    def render_scene(self):
        zw = 100
        zdir = -1

        image = Image.new('RGB', (self.vp.hres, self.vp.vres), (0, 0, 0))
        draw = ImageDraw.Draw(image)

        for r in range(self.vp.vres):
            for c in range(self.vp.hres):
                x = self.vp.s * (r - 0.5 * (self.vp.hres - 1))
                y = self.vp.s * (c - 0.5 * (self.vp.vres - 1))
                ray = Ray()
                ray.setOriginXYZ(x, y, zw)
                ray.setDirXYZ(0, 0, zdir)
                # pixel = self.tracer.trace_ray(ray)
                pixel = self.mul_tracer.trace_ray(ray)
                draw.point((r, c), fill=(pixel.r, pixel.g, pixel.b))

        image.save('code.jpg', 'jpeg')


world = World()
world.render_scene()
