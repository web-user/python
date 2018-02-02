from random import Random

from transformsettings import TransformSettings
import transform

class TransformFactory(object):

    CLASSES = [
        'LinearTransform',
        'SinTransform',
        'SphereTransform',
        'PolarTransform',
        'HeartTransform',
        'DiskTransform'
    ]

    def __init__(self, randomizer=Random()):
        self.randomizer = randomizer

    def get_random_transformation(self):
        conf = TransformSettings.init_random()

        index = self.randomizer.randint(0, len(self.CLASSES) - 1)
        class_name = self.CLASSES[index]

        return self.get_transformation(class_name, conf)

    @staticmethod
    def get_transformation(class_name, conf):
        if hasattr(transform, class_name):
            return getattr(transform, class_name)(conf)
        else:
            return None
