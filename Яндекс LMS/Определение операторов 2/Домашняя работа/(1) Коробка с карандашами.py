class Pencil:

    def __init__(self, length, thick, color):
        self.length = length
        self.thick = thick
        self.color = color

    def __repr__(self):
        return f"Pencil({self.length=}, {self.thick=}, {self.color=})".replace("self.", "")

    def __eq__(self, other):
        return self.length == other.length and self.thick == other.thick and self.color == other.color


class PencilBox:

    def __init__(self, length, thick, box):
        self.length = length
        self.thick = thick
        self.box = box

    def get(self):
        suitable = []
        colors = set()
        for pencil in self.box:
            if pencil.length == self.length and pencil.thick == self.thick and pencil.color not in colors:
                colors.add(pencil.color)
                suitable.append(pencil)
        suitable.sort(key=lambda x: x.color)
        return suitable

    def __repr__(self):
        return f"PencilBox({self.length=}, {self.thick=}, {self.box=})".replace("self.", "")

    def __eq__(self, other):
        return self.length == other.length and self.thick == other.thick and self.box == other.box

