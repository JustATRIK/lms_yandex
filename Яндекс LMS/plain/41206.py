from collections import defaultdict


class TypeStatistics:

    def __init__(self, data):
        self.data = data

    def type_values(self):
        types = defaultdict(list)
        for value in self.data:
            types[value.__class__.__name__].append(value)
        return dict(types)

    def type_counts(self):
        types = defaultdict(int)
        for value in self.data:
            types[value.__class__.__name__] += 1
        return dict(types)
