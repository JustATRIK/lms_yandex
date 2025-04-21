import math


class FlowingRectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        if width == 0 or height == 0:
            self.ratio = 0
        else:
            self.ratio = width / height

    def __add__(self, other):
        new_area = self.width * self.height + other.width * other.height
        if new_area == 0:
            self.width = 0
            self.height = 0
            return self
        if self.ratio == 0:
            self.ratio = other.ratio
        new_height = math.sqrt(new_area / self.ratio)
        new_width = new_height * self.ratio
        self.width = new_width
        self.height = new_height
        return self

    def __sub__(self, other):
        new_area = self.width * self.height - other.width * other.height
        if new_area <= 0:
            self.width = 0
            self.height = 0
            return self
        if self.ratio == 0:
            self.ratio = other.ratio
        new_height = math.sqrt(new_area / self.ratio)
        new_width = new_height * self.ratio
        self.width = new_width
        self.height = new_height
        return self

    def get_width(self):
        return round(self.width, 2)

    def get_height(self):
        return round(self.height, 2)
