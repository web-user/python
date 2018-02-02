import math
from transformsettings import TransformSettings
from transformfactory import TransformFactory

class Transform(object):

    def __init__(self, conf):
        self.conf = conf

    def _get_affine_transformation(self, (x, y)):
        new_x = self.conf.a * x + self.conf.b * y + self.conf.c
        new_y = self.conf.d * x + self.conf.e * y + self.conf.f
        return new_x, new_y

    def get_new_point(self, (x, y)):
        raise NotImplemented('Method has to be implemented in subclasses.')

    def serialize(self):
        return {
            'type': type(self).__name__,
            'conf': self.conf.serialize()
        }

    @staticmethod
    def deserialize(obj):
        conf = TransformSettings.deserialize(obj['conf'])
        return TransformFactory.get_transformation(obj['type'], conf)


class LinearTransform(Transform):

    def get_new_point(self, (x, y)):
        return self._get_affine_transformation((x, y))


class SinTransform(Transform):

    def get_new_point(self, (x, y)):
        x, y = self._get_affine_transformation((x, y))
        new_x = math.sin(x)
        new_y = math.sin(y)
        return new_x, new_y


class SphereTransform(Transform):

    def get_new_point(self, (x, y)):
        x, y = self._get_affine_transformation((x, y))
        new_x = x / (x**2 + y**2)
        new_y = y / (x**2 + y**2)
        return new_x, new_y


class PolarTransform(Transform):

    def get_new_point(self, (x, y)):
        x, y = self._get_affine_transformation((x, y))
        new_x = math.atan2(y, x) / math.pi
        new_y = math.sqrt(x**2 + y**2) - 1
        return new_x, new_y


class HeartTransform(Transform):

    def get_new_point(self, (x, y)):
        x, y = self._get_affine_transformation((x, y))
        r = math.sqrt(x*x + y*y)
        theta = math.atan2(y, x)
        new_x = r * math.sin(theta * r)
        new_y = -r * math.cos(theta * r)
        return new_x, new_y


class DiskTransform(Transform):

    def get_new_point(self, (x, y)):
        x, y = self._get_affine_transformation((x, y))
        r = math.sqrt(x*x + y*y) * math.pi
        theta = math.atan2(y, x) / math.pi
        new_x = theta * math.sin(r)
        new_y = theta * math.cos(r)
        return new_x, new_y
