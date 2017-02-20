from vector import Vector


class Ray(object):

    def __init__(self):
        self.origin = Vector()
        self.dir = Vector()

    def setOrigin(self, origin):
        self.origin.set(origin)

    def setOriginXYZ(self, x, y, z):
        self.origin.x = x
        self.origin.y = y
        self.origin.z = z

    def setDir(self, dir):
        self.dir.set(dir)

    def setDirXYZ(self, x, y, z):
        self.dir.x = x
        self.dir.y = y
        self.dir.z = z

ray = Ray()
