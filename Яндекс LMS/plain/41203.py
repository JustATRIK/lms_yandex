import math


class Square:

    def __init__(self, side):
        self.side = side

    def extrude(self, h):
        area = self.side ** 2
        return area * h


class Rectangle:

    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def extrude(self, h):
        area = self.side1 * self.side2
        return area * h


class Triangle:

    def __init__(self, side):
        self.side = side

    def extrude(self, h):
        area = (math.sqrt(3) / 4) * self.side ** 2
        return area * h


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def extrude(self, h):
        area = math.pi * self.radius ** 2
        return area * h
