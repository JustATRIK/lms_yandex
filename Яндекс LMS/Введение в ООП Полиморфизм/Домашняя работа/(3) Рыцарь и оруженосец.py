class Human:

    def __init__(self, name, *weapon):
        self.name = name
        self.weapons = list(weapon)

    def info(self):
        return f"{self.__class__.__name__}({self.name})"

    def fight(self, weapon):
        if weapon in self.weapons:
            return "".join([i for i in weapon if i not in "aoeiuy"])
        return None


class Knight(Human):

    def announce(self, lady):
        return f"Long live the noblest {lady}!"

    def fight(self, weapon):
        sound = super().fight(weapon)
        return sound.upper() if sound is not None else None


class Squire(Human):

    def __init__(self, name, knight, *weapon):
        super().__init__(name, *weapon)
        self.knight = knight

    def praise(self):
        return f"Glory to {self.knight}!"

