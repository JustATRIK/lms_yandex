class Interaction:

    def __init__(self, carrier="", constanta=0):
        self.carrier = carrier
        self.const = constanta

    def __str__(self):
        return f"{self.__class__.__name__}('{self.carrier}', {self.const})"


class Gravitational(Interaction):

    def __init__(self):
        super().__init__("graviton", 1e-39)


class Electromagnetic(Interaction):

    def __init__(self):
        super().__init__("photon", 1 / 137)


class Strong(Interaction):

    def __init__(self):
        super().__init__("photon", 1)


class Weak(Interaction):

    def __init__(self):
        super().__init__("boson", 1e-15)


class ForceOfUniversalGravity(Gravitational):

    def __init__(self):
        super().__init__()
        self.G = 6.67e-11

    def __call__(self, val1, val2, r):
        return self.G * val1 * val2 / r ** 2


class CoulombPower(Electromagnetic):

    def __init__(self):
        super().__init__()
        self.k = 9e9

    def __call__(self, val1, val2, r):
        return self.k * val1 * val2 / r ** 2


class FrictionForce(Electromagnetic):

    def __init__(self, q):
        super().__init__()
        self.q = q

    def __call__(self, N):
        return N * self.q
