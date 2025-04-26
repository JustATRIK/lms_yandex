class Wardrobe:

    def __init__(self, *items):
        self.items = items

    def __str__(self):
        return " ".join(self.items)

    def __eq__(self, other):
        return isinstance(self, other.__class__) and len(self.items) == len(other.items)

    def __lt__(self, other):
        if isinstance(self, other.__class__):
            return len(self.items) < len(other.items)
        return isinstance(other, MagicWardrobe)

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return other <= self


class JustWardrobe(Wardrobe):

    def __str__(self):
        items = list(self.items)
        items[0] = items[0].title()
        return ", ".join(items) + "."


class MagicWardrobe(Wardrobe):

    def __str__(self):
        return ", ".join(sorted(map(lambda x: x.title(), self.items))) + "."
