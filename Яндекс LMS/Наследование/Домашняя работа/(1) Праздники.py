class Holiday:
    _months = ["March", "April", "May", "June", "July", "August", "September", "October", "November", "December",
               "January", "February"]
    _seasons = ["Spring", "Summer", "Autumn", "Winter"]

    def __init__(self, name, date):
        self.name = name
        self.date = date

    def __str__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.date}')"

    def get_season(self):
        return self._seasons[self._months.index(self.date.split()[1]) // 3]


class NewYear(Holiday):

    def __init__(self, name, date, people):
        super().__init__(name, date)
        self.people = people.copy()

    def congratulate(self, name):
        if name in self.people:
            return f"Dear {name}! Happy New Year!"
        self.people.append(name)
        return f"Dear new friend {name}! Have fun this New Year!"

    def get_greet(self):
        return self.people


class MuseumDay(Holiday):

    def __init__(self, name, date, museums):
        super().__init__(name, date)
        self.museums = museums

    def get_museums(self):
        return self.museums

