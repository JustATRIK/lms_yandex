class Wagon:

    def __init__(self, num):
        self.num = num

    def get_number(self):
        return self.num

    def __str__(self):
        return f"№{self.num}"


class Train:

    def __init__(self, num, wagons=None):
        self.num = num
        self.wagons = []
        if wagons is not None:
            self.wagons += wagons

    def get_number(self):
        return self.num

    def get_wagons(self):
        return self.wagons

    def append(self, wagon):
        self.wagons.append(wagon)

    def __len__(self):
        return len(self.wagons)

    def __str__(self):
        return f"Train {self.get_number()} has {len(self)} wagons"

    def __getitem__(self, item):
        return self.wagons[item]

    def __setitem__(self, key, value):
        self.wagons[key] = value

    def __delitem__(self, key):
        if key == len(self) - 1:
            self.wagons.pop()

    def __iter__(self):
        return iter(self.wagons)
