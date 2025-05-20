class NestingDoll:

    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"Russian Folk doll, size {self.get_size()}."

    def get_size(self):
        return self.size


class OrdinaryNestingDoll(NestingDoll):

    def __init__(self, size, step):
        super().__init__(size)
        self.step = step

    def previous_doll(self):
        return OrdinaryNestingDoll(self.size + self.step, self.step)

    def next_doll(self):
        if self.size - self.step <= 0:
            return SmallestNestingDoll(self.size, self.step)
        return OrdinaryNestingDoll(self.size - self.step, self.step)


class SmallestNestingDoll(OrdinaryNestingDoll):

    def next_doll(self):
        return None
