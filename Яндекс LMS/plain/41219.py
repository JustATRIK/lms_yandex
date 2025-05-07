class PearsBasket:

    def __init__(self, count):
        self.count = count

    def __floordiv__(self, other):
        arr = []
        for i in range(other):
            arr.append(PearsBasket(self.count // other))
        if self.count % other != 0:
            arr.append(PearsBasket(self.count % other))
        return arr

    def __add__(self, other):
        return PearsBasket(self.count + other.count)

    def __sub__(self, other):
        self.count -= other
        self.count = max(0, self.count)

    def __mod__(self, other):
        return self.count % other

    def __str__(self):
        return str(self.count)

    def __repr__(self):
        return f"PearsBasket({self.count})"

