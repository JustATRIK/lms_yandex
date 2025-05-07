class ModularArithmetic:

    def __init__(self, value, mod):
        self.value = value % mod
        self.mod = mod

    def __add__(self, other):
        return ModularArithmetic(self.value + other.value, self.mod)

    def __sub__(self, other):
        return ModularArithmetic(self.value - other.value, self.mod)

    def __str__(self):
        return f"{self.value}({self.mod})"

    def __repr__(self):
        return str(self)

    def __rshift__(self, other):
        return ModularArithmetic(self.value + (other % self.mod), self.mod)

    def __lshift__(self, other):
        return ModularArithmetic(self.value - (other % self.mod), self.mod)

    def __call__(self, val):
        return val // self.mod

