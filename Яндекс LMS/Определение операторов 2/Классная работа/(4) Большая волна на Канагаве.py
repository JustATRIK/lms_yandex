class BigWave:

    def __init__(self, *items, freq=-1):
        self.items = list(items)
        self.freq = freq

    def __getitem__(self, item):
        return self.items[item]

    def __len__(self):
        return len(self.items)

    def __setitem__(self, key, value):
        self.items[key] = value

    def pop(self, ind=None):
        if ind is None:
            return self.items.pop()
        return self.items.pop(ind)

    def success(self):
        return list(filter(lambda x: x % self.freq == 0, self.items))

    def fail(self):
        return list(filter(lambda x: x % self.freq != 0, self.items))

    def __repr__(self):
        return f"BigWave({', '.join(map(str, self.items))}, {self.freq=})".replace("self.", "")
