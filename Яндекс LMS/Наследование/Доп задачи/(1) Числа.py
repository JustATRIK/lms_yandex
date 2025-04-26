class NaturalNumber:

    def __init__(self, value):
        if self.__class__ == NaturalNumber:
            self.value = max(value, 0)
        else:
            self.value = value

    def __add__(self, other):
        if issubclass(self.__class__, other.__class__):
            return self.__class__(self.value + other.value)
        return other.__class__(self.value + other.value)

    def __sub__(self, other):
        if issubclass(self.__class__, other.__class__):
            return self.__class__(self.value - other.value)
        return other.__class__(self.value - other.value)

    def __str__(self):
        return f"{self.__class__.__name__}({self.value})"


class Integer(NaturalNumber):
    pass


class RealNumber(Integer):
    pass


class ComplexNumber(RealNumber):

    def __str__(self):
        return f"{self.__class__.__name__}({self.value})"
