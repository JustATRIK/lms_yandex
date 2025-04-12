class Megalith:

    def __init__(self, data):
        self.data = data

    def middle(self):
        return self.data[len(self.data) // 2]

    def lowest(self):
        return min(self.data)

    def highest(self):
        return max(self.data)

    def median(self):
        return sorted(self.data)[len(self.data) // 2]
