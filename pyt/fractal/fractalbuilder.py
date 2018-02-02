from random import Random
from math import log10
from PIL import Image
from time import time

from pixel import Pixel
from transformfactory import TransformFactory
from transform import Transform


class FractalBuilder(object):

    XMIN = -1
    XMAX = 1
    YMIN = -1
    YMAX = 1
    GAMMA = 2.2

    def __init__(self, width, height,
                 seed=time(), points=1000, iterations=5000,
                 transformations=None):
        self.width = width
        self.height = height
        self._seed = seed

        self._points = points
        self._iterations = iterations
        self._init_transformations(transformations)

        self._pixels = None

    def _init_transformations(self, transformations):
        if transformations is not None:
            self._transformations = transformations
            self._trans_count = len(self._transformations)
        else:
            rand = Random()
            generator = TransformFactory(rand)
            self._trans_count = rand.randint(5, 10)
            self._transformations = [generator.get_random_transformation()
                                    for i in xrange(self._trans_count)]

    def build(self):
        rand = Random(self._seed)

        self._pixels = [[Pixel() for i in xrange(self.height)]
                        for j in xrange(self.width)]

        for point in xrange(self._points):
            x = rand.uniform(self.XMIN, self.XMAX)
            y = rand.uniform(self.YMIN, self.YMAX)

            for step in xrange(self._iterations + 20):
                trans_index = rand.randint(0, self._trans_count - 1)
                transform = self._transformations[trans_index]
                x, y = transform.get_new_point((x, y))

                if step >= 20 and \
                        self.XMIN <= x <= self.XMAX and \
                        self.YMIN <= y <= self.YMAX:
                    xpos, ypos = self._get_real_point((x, y))

                    if xpos < self.width and ypos < self.height:
                        self._pixels[xpos][ypos].hit(transform.conf.color)

        self._correct()

    def _get_real_point(self, (x, y)):
        xshift = ((self.XMAX - x) / (self.XMAX - self.XMIN)) * self.width
        yshift = ((self.YMAX - y) / (self.YMAX - self.YMIN)) * self.height
        return self.width - int(xshift), self.height - int(yshift)

    def _correct(self):
        max_ = 0.0
        ungamma = 1.0 / self.GAMMA

        for row in xrange(self.width):
            for col in xrange(self.height):
                if self._pixels[row][col].hits != 0:
                    self._pixels[row][col].normal = log10(self._pixels[row][col].hits)
                    if self._pixels[row][col].normal > max_:
                        max_ = self._pixels[row][col].normal

        for row in xrange(self.width):
            for col in xrange(self.height):
                pixel = self._pixels[row][col]

                pixel.normal /= max_
                r = int(pixel.color[0] * (pixel.normal ** ungamma))
                g = int(pixel.color[1] * (pixel.normal ** ungamma))
                b = int(pixel.color[2] * (pixel.normal ** ungamma))

                pixel.color = (r, g, b)

    def get_image(self):
        img = Image.new('RGB', (self.width, self.height))

        for i in xrange(self.width):
            for j in xrange(self.height):
                img.putpixel((i, j), self._pixels[i][j].color)

        return img

    def serialize(self):
        transformations = []
        for transform in self._transformations:
            transformations.append(transform.serialize())

        fractal = {
            'height': self.height,
            'width': self.width,
            'seed': self._seed,
            'points': self._points,
            'iterations': self._iterations,
            'transformations': transformations
        }

        return fractal

    @classmethod
    def deserialize(cls, obj):
        transformations = []
        for transform in obj['transformations']:
            transformations.append(Transform.deserialize(transform))

        return cls(obj['width'], obj['height'],
                   obj['seed'], obj['points'], obj['iterations'],
                   transformations)
