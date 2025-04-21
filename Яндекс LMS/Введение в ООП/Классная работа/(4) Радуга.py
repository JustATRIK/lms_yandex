class Rainbow:

    _colors = "red, orange, yellow, green, light blue, blue, violet".split(", ")

    def __init__(self, rb_type=1):
        self.reverse = rb_type == 2

    def next_color(self, color):
        ind = self._colors.index(color) + (-1 if self.reverse else 1)
        if ind == -1:
            ind = 6
        elif ind == 7:
            ind = 0
        return self._colors[ind]

