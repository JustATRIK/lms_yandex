class LineToTable:

    def __init__(self, lst, rows, cols):
        self.lst = lst
        self.rows = rows
        self.cols = cols

    def resize(self):
        matrix = [self.lst[i * self.cols: (i + 1) * self.cols] for i in range(self.rows)]
        return matrix, self.rows, self.cols


class TableToLine:

    def __init__(self, matrix):
        self.matrix = matrix

    def resize(self):
        line = []
        for row in self.matrix:
            line.extend(row)
        n = len(self.matrix)
        m = len(self.matrix[0]) if n else 0
        return line, n, m
