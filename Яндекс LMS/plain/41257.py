class Fish:

    @staticmethod
    def all_about_me():
        return "I'm a fish and I'm swimming"


class Amphibians:

    @staticmethod
    def all_about_me():
        return "I can crawl"


class Anabas(Fish, Amphibians):
    ...


class Salamander(Amphibians, Fish):
    ...

