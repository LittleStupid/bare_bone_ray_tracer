from vector import Vector
import math

SPHERE_ERR = 0.0001


class Sphere(object):

    def __init__(self, pos, r):
        self.pos = Vector()
        self.pos.set(pos)
        self.r = r

    def hit(self, ray):
        center_diff = ray.origin - self.pos
        a = ray.dir * ray.dir
        b = 2 * (ray.dir * center_diff)
        c = center_diff * center_diff - self.r * self.r
        delta = b * b - 4 * (a * c)

        # if(ray.origin.x < 0 and ray.origin.y < 0):
        #     print('hit: %s' % self.pos.x, self.pos.y,
        #           self.pos.z, self.r)
        #     print('origin %s' % ray.origin.x, ray.origin.y, ray.origin.z)
        #     print('dir %s' % ray.dir.x, ray.dir.y, ray.dir.z)
        #     print('-----')
        if delta < 0:
            # print('sphere pos: %s' % self.pos)
            # print('sphere r: %s' % self.r)
            # print('ray origin: %s' % ray.origin)
            # print('ray dir: %s' % ray.dir)
            # print('a:b:c:delta %s' % a, b, c, delta)
            return {'hit': False}

        e = math.sqrt(delta)

        t = (-b - e) / (2 * a)
        if(t > SPHERE_ERR):
            return {'hit': True, 'tmin': t}

        t = (-b + e) / (2 * a)
        if(t > SPHERE_ERR):
            return {'hit': True, 'tmin': t}

        return {'hit': False}
