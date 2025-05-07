class GiftSet:

    def __init__(self, *gifts):
        self.gifts = list(gifts)

    def __floordiv__(self, number):
        n = len(self.gifts)
        m = n // number
        k = m * number
        new_sets = []
        for i in range(number):
            part = self.gifts[i * m:(i + 1) * m]
            new_sets.append(GiftSet(*part))
        self.gifts = self.gifts[k:]
        return new_sets

    def __iadd__(self, other):
        self.gifts.extend(other)
        return self

    def cost(self):
        total = sum(self.gifts)
        k = len(self.gifts)
        if k == 0:
            return 0
        discount = (k - 1) * 0.05
        discount = min(discount, 0.5)
        multiplier = 1 - discount
        return int(round(total * multiplier, 3))

    def get_gifts(self):
        return self.gifts
