class Mirror:

    def __init__(self, matrix):
        self.matrix = matrix.copy()

    def reflect(self):
        ...


class RightMirror(Mirror):

    def reflect(self):
        for i, arr in enumerate(self.matrix):
            self.matrix[i] = arr[::-1]


class BottomMirror(Mirror):

    def reflect(self):
        for i in range(len(self.matrix) // 2):
            j = len(self.matrix) - 1 - i
            self.matrix[i], self.matrix[j] = self.matrix[j], self.matrix[i]

