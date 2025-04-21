class Robot:

    _dirs = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}

    def __init__(self, start):
        self.pos = start
        self._path = [start]

    def move(self, path):
        self._path.clear()
        for p in path:
            self._path.append(self.pos)
            self.pos = (self.pos[0] + self._dirs[p][0], self.pos[1] + self._dirs[p][1])
        self._path.append(self.pos)
        return self.pos

    def path(self):
        return self._path
