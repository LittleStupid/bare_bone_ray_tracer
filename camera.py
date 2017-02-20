from vector import Vector
from world import World
from view_plane import ViewPlane
from PIL import Image, ImageDraw
from ray import Ray


class Camera(object):

    def __init__(self):
        self.up = Vector()
        self.eye = Vector()
        self.lookat = Vector()
        # self.uvw = Vector()
        self.u = Vector()
        self.v = Vector()
        self.w = Vector()

    def compute_uvw(self):
        w = self.eye - self.lookat
        w.normalize()

        u = up.cross(w)
        w.normalize()

        v = w.cross(v)

    def render_scene(self, world):
        zw = 100
        zdir = -1
        vp = ViewPlane()

        image = Image.new('RGB', (vp.hres, vp.vres), (0, 0, 0))
        draw = ImageDraw.Draw(image)

        for r in range(vp.vres):
            for c in range(vp.hres):
                x = vp.s * (r - 0.5 * (vp.hres - 1))
                y = vp.s * (c - 0.5 * (vp.vres - 1))
                ray = Ray()
                ray.setOriginXYZ(x, y, zw)
                ray.setDirXYZ(0, 0, zdir)
                pixel = world.mul_tracer.trace_ray(ray).color
                draw.point((r, c), fill=(pixel.r, pixel.g, pixel.b))

        image.save('camera.jpg', 'jpeg')

cam = Camera()
cam.render_scene(World())
