class Blues:

    def __init__(self, *notes):
        self.notes = list(notes)

    def __add__(self, other):
        return Blues(*(self.notes + other.notes))

    def __iadd__(self, other):
        self.notes.append(other)
        return self

    def __str__(self):
        return "-".join(self.notes)

