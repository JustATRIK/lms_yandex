class Potato:

    def __init__(self, size):
        self.size = size

    def __truediv__(self, other):
        ns = self.size / other
        self.size -= ns
        return Potato(ns)

    def __itruediv__(self, other):
        self.size /= other
        return self

    def __str__(self):
        return f"Potato({self.size})"

