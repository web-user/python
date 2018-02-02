from random import uniform, randint


class TransformSettings(object):

    MIN_COLOR = 64
    MAX_COLOR = 255

    def __init__(self, a, b, c, d, e, f, color):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.color = color

    @staticmethod
    def init_random():
        conf = TransformSettings(0, 0, 0, 0, 0, 0, None)
        conf.generate_coefs()
        conf.generate_color()
        return conf

    def check_coefs(self):
        a = self.a
        b = self.b
        d = self.d
        e = self.e

        return (-1 <= a <= 1) and \
            (-1 <= b <= 1) and \
            (-1 <= d <= 1) and \
            (-1 <= e <= 1) and \
            (a ** 2 + d ** 2 < 1) and \
            (b ** 2 + e ** 2 < 1) and \
            (a**2 + b**2 + d**2 + e**2 < 1 + (a*e - b*d) ** 2)

    def generate_coefs(self):
        while True:
            self.a = uniform(-1, 1)
            self.b = uniform(-1, 1)
            self.d = uniform(-1, 1)
            self.e = uniform(-1, 1)

            if self.check_coefs():
                break

        self.c = uniform(-1, 1)
        self.f = uniform(-1, 1)

    def generate_color(self):
        min_ = TransformSettings.MIN_COLOR
        max_ = TransformSettings.MAX_COLOR
        r = randint(min_, max_)
        g = randint(min_, max_)
        b = randint(min_, max_)
        self.color = (r, g, b)

    def serialize(self):
        return {
            'a': self.a,
            'b': self.b,
            'c': self.c,
            'd': self.d,
            'e': self.e,
            'f': self.f,
            'cr': self.color[0],
            'cg': self.color[1],
            'cb': self.color[2]
        }

    @classmethod
    def deserialize(cls, obj):
        return cls(obj['a'], obj['b'], obj['c'], obj['d'], obj['e'], obj['f'],
                   (obj['cr'], obj['cg'], obj['cb']))
