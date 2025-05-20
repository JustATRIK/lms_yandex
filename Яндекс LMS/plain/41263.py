class Cucumber:

    def crunch(self):
        return "crunch"

    def refresh(self):
        return "Cucumber refresh."


class Tomato:

    def melt(self):
        return "melt in the mouth"

    def refresh(self):
        return "Tomato refresh."


class Salad(Tomato, Cucumber):
    ...


class Smoothie(Cucumber, Tomato):
    ...
