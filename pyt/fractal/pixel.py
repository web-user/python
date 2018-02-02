from math import log10

class Pixel(object):

    def __init__(self, color=(0, 0, 0)):
        self.color = color
        self.hits = 0
        self.normal = 0

    def hit(self, color):
        if self.hits == 0:
            self.color = color
        else:
            r = (self.color[0] + color[0]) / 2
            g = (self.color[1] + color[1]) / 2
            b = (self.color[2] + color[2]) / 2
            self.color = (r, g, b)

        self.hits += 1

