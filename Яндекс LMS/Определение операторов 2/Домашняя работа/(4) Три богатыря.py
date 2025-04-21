class EpicHero:

    def __init__(self, name, number_of_wins, list_of_weapons):
        self.name = name
        self.number_of_wins = number_of_wins
        self.list_of_weapons = sorted(list_of_weapons.copy())

    def __str__(self):
        return f"Epic Hero {self.name}, {self.number_of_wins}"

    def __repr__(self):
        return f"EpicHero('{self.name}', {self.number_of_wins}, {self.list_of_weapons})"

    def add_win(self):
        self.number_of_wins += 1

    def add_weapon(self, item):
        self.list_of_weapons.append(item)
        self.list_of_weapons.sort()

    def del_weapon(self, item):
        if item in self.list_of_weapons:
            self.list_of_weapons.remove(item)

    def __eq__(self, other):
        return (self.number_of_wins, len(self.list_of_weapons), -len(self.name), self.name) == (
            other.number_of_wins, len(other.list_of_weapons), -len(other.name), other.name)

    def __lt__(self, other):
        return (self.number_of_wins, len(self.list_of_weapons), -len(self.name), self.name) < (
            other.number_of_wins, len(other.list_of_weapons), -len(other.name), other.name)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return other <= self

    def __ge__(self, other):
        return other < self
