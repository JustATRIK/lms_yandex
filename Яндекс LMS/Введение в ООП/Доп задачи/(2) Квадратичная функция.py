class Quadratic:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def branch(self):
        return "up" if self.a >= 0 else "down"

    def x_sect(self):
        a = self.sections()
        if a is None:
            return 0
        return len(a) // 2

    def sections(self):
        d = self.b ** 2 - 4 * self.a * self.c
        if d < 0:
            return None
        elif d == 0:
            return -self.b / (2 * self.a), 0
        else:
            d = d ** 0.5
            x1, x2 = (-self.b - d) / (2 * self.a), (-self.b + d) / (2 * self.a)
            return min(x1, x2), 0, max(x1, x2), 0

    def top(self):
        x = -self.b / (2 * self.a)
        return x, self.a * x ** 2 + self.b * x + self.c

    def y_sect(self):
        return 0, self.c
