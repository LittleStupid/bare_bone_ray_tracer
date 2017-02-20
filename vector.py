from err import InvalidTypeError


class Vector(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def equal(self, that):
        if that is None:
            return False

        if False == isinstance(that, Vector):
            raise(InvalidTypeError('Invalid type error: %s' % type(that)))

        if self.x != that.x:
            return False

        if self.y != that.y:
            return False

        if self.z != that.z:
            return False

        return True
