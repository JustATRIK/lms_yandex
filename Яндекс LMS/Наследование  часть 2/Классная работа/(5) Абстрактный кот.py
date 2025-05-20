class AbstractCat:

    def __init__(self):
        self.size = 0
        self.left = 0

    def eat(self, food):
        food += self.left
        self.left = food % 10
        self.size += food // 10
        self.size = min(self.size, 100)

    def __str__(self):
        return f"{self.__class__.__name__} ({self.size})"

    def meow(self):
        pass


class Kitten(AbstractCat):

    def __init__(self, size):
        super().__init__()
        self.size = size

    def sleep(self):
        return "Snore" * (self.size // 5)

    def meow(self):
        return "meow..."


class Cat(Kitten):

    def __init__(self, size, name):
        super().__init__(size)
        self.name = name

    def get_name(self):
        return self.name

    def meow(self):
        return "MEOW..."
    
    def catch_mice(self):
        return "Got it!"
