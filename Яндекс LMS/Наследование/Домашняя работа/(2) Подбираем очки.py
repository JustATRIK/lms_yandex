import math


class Glasses:

    def __init__(self, mode=1, dist=64, sun=False, d=0.0):
        self.mode = mode
        self.dist = dist
        self.sun = sun
        self.d = d

    def focus(self):
        if self.d == 0.0:
            return math.inf
        return round(100 / self.d, 1)

    def __str__(self):
        return f"{self.__class__.__name__}({self.mode}, {self.dist}, {self.sun}, {self.d})"


class NearSightedNess(Glasses):

    def __init__(self, mode=1, dist=64, sun=False, dl=0.0, dr=0.0):
        super().__init__(mode, dist, sun, dr if abs(dr) > abs(dl) else dl)

    def best_vision_distance(self):
        if self.d == 0.0:
            return math.inf
        return abs(round(100 / self.d, 1))


class FarSightedNess(Glasses):

    def __init__(self, mode=1, dist=64, sun=False, dl=0.0, dr=0.0):
        super().__init__(mode, dist, sun, max(dr, dl))

