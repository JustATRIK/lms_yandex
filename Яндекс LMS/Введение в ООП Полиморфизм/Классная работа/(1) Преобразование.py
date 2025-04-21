from math import pi


class SquareIntoCircle:

    def __init__(self, length):
        self.length = length

    def size(self):
        radius = (2 * self.length) / pi
        return round(radius, 3)

    def area(self):
        radius = (2 * self.length) / pi
        area = pi * (radius ** 2)
        return round(area, 3)


class CircleIntoSquare:

    def __init__(self, radius):
        self.radius = radius

    def size(self):
        side = (pi * self.radius) / 2
        return round(side, 3)

    def area(self):
        side = (pi * self.radius) / 2
        area = side ** 2
        return round(area, 3)
