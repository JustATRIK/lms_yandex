class Mosquito:

    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"{self.__class__.__name__}, {self.age} days"


class MaleMosquito(Mosquito):

    def __init__(self, age):
        super().__init__(age)
        self.age = age
        self.feed = "nectar"
        self.lives = "on land"

    def hearing(self):
        return f"I hear and see everything {self.lives}"


class FemaleMosquito(Mosquito):

    def __init__(self, age):
        super().__init__(age)
        self.age = age
        self.feed = "blood"
        self.lives = "on land"

    def squeak(self):
        return f"The thin squeak of a mosquito after eating {self.feed}"


class MosquitoLarva(MaleMosquito, FemaleMosquito):

    def __init__(self, age):
        super().__init__(age)
        self.feed = "algae"
        self.lives = "in water"
