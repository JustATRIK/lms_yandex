class ClassicalMechanics:

    def __init__(self, v):
        self.v = v

    def __call__(self, v1):
        return self.calculate(v1)

    def calculate(self, v1):
        return self.v + v1

    def __str__(self):
        return f"Object {self.__class__.__name__}, velocity {self.v} с"


class SpecialTheoryRelativity(ClassicalMechanics):

    def calculate(self, v1):
        if v1 < 0.1 and self.v < 0.1:
            return super().calculate(v1)
        return super().calculate(v1) / (1 + self.v * v1)
