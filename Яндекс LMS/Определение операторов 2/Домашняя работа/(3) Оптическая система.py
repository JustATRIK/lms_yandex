class OpticSystem:

    def __init__(self, arr):
        self.arr = arr.copy()

    def __add__(self, other):
        return OpticSystem(self.arr + other.arr)

    def append(self, val):
        self.arr.append(val)

    def __iadd__(self, other):
        self.arr += other.arr
        return self

    def __rshift__(self, other):
        return self << len(self) - other

    def __lshift__(self, other):
        shift_val = other % len(self.arr)
        arr1 = self.arr[:shift_val]
        arr2 = self.arr[shift_val:]
        self.arr = arr2 + arr1
        return self.arr

    def __iter__(self):
        return iter(self.arr)

    def __call__(self, dist):
        if sum(self) - 1 / dist == 0:
            return None
        return round(1 / (sum(self) - 1 / dist), 4)

    def __getitem__(self, item):
        return self.arr[item]

    def __setitem__(self, key, value):
        self.arr[key] = value

    def __len__(self):
        return len(self.arr)

    def __delitem__(self, key):
        self.arr.pop(key)

    def __lt__(self, other):
        if sum(self) == sum(other):
            return len(self) < len(other)
        return sum(self) < sum(other)

    def __le__(self, other):
        if sum(self) == sum(other):
            return len(self) <= len(other)
        return sum(self) <= sum(other)

    def __gt__(self, other):
        return other <= self.arr

    def __ge__(self, other):
        return other < self.arr

    def __eq__(self, other):
        return sum(self) == sum(other) and len(self) == len(other)
