class JamesWebb:

    def __init__(self, data):
        self.data = data

    def brightest_star(self):
        coords = ()
        max_value = 0
        for x in range(len(self.data)):
            for y in range(len(self.data[x])):
                val = self.data[x][y]
                if val < 0 and abs(val) > max_value:
                    max_value = abs(val)
                    coords = (x, y)
        return coords

    def brightest_galaxy(self):
        coords = ()
        max_value = 0
        for x in range(len(self.data)):
            for y in range(len(self.data[x])):
                val = self.data[x][y]
                if val > 0 and abs(val) > max_value:
                    max_value = abs(val)
                    coords = (x, y)
        return coords

    def stars(self):
        count = 0
        for x in self.data:
            for y in x:
                if y < 0:
                    count += 1
        return count

    def galaxies(self):
        count = 0
        for x in self.data:
            for y in x:
                if y > 0:
                    count += 1
        return count

    def voids(self):
        count = 0
        for x in self.data:
            for y in x:
                if y == 0:
                    count += 1
        return count
