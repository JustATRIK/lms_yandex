class Hyperbole:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, x):
        if x == 0:
            return None
        return round(self.a + self.b / x, 6)

    def __repr__(self):
        return f"Hyp({self.a}, {self.b})"

    def __str__(self):
        return f"y = {self.a} + {self.b}/x"
