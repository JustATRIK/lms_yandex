class ModifiedString:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return ModifiedString(self.value + other)

    def __radd__(self, other):
        return ModifiedString(other + self.value)

    def __sub__(self, other):
        ign = set(other.lower())
        return ModifiedString("".join([i for i in self.value if i.lower() not in ign]))

    def __rsub__(self, other):
        ign = set(self.value.lower())
        return ModifiedString("".join([i for i in other if i.lower() not in ign]))

    def __str__(self):
        return self.value

