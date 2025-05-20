class Seat:

    def __init__(self, size, color):
        self.size = size
        self.color = color

    def __str__(self):
        return f"{self.__class__.__name__}({', '.join(map(str, self.__dict__.values()))})"


class Chair(Seat):

    def __init__(self, size, color, height, legs_count):
        super().__init__(size, color)
        self.height = height
        self.legs_count = legs_count


class ArmChair(Seat):

    def __init__(self, size, color, height, material):
        super().__init__(size, color)
        self.height = height
        self.material = material


class Stool(Seat):

    def __init__(self, size, color, legs_count):
        super().__init__(size, color)
        self.legs_count = legs_count


class BagChair(Seat):

    def __init__(self, size, color, material):
        super().__init__(size, color)
        self.material = material
