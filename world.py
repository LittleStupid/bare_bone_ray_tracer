from view_plane import ViewPlane
from sphere import Sphere
from vector import Vector
from tracer import SphereTracer
from ray import Ray
from PIL import Image, ImageDraw


class World(object):

    def __init__(self):
        self.vp = ViewPlane()

        pos = Vector()
        self.sphere = Sphere(pos, 128)

        self.tracer = SphereTracer(self)

    def render_scene(self):
        zw = 100
        zdir = -1

        image = Image.new('RGB', (self.vp.hres, self.vp.vres), (0, 0, 0))
        draw = ImageDraw.Draw(image)

        for r in range(self.vp.vres):
            for c in range(self.vp.hres):
                x = self.vp.s * (c - 0.5 * (self.vp.hres - 1))
                y = self.vp.s * (r - 0.5 * (self.vp.vres - 1))
                ray = Ray()
                ray.setOriginXYZ(x, y, zw)
                ray.setDirXYZ(x, y, zdir)
                pixel = self.tracer.trace_ray(ray)
                draw.point((r, c), fill=(pixel.r, pixel.g, pixel.b))

        image.save('code.jpg', 'jpeg')


world = World()
world.render_scene()
