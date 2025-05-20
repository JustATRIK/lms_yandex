class Board:

    def __init__(self, rows, columns, filler1="0"):
        self.board = [filler1 * columns for _ in range(rows)]

    def __str__(self):
        return "\n".join(self.board)


class Checker(Board):

    def __init__(self, size, filler2, filler1="0"):
        super().__init__(size, size, filler1)
        for i in range(size):
            for j in range(size):
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                    self.board[i] = self.board[i][:j] + filler2 + self.board[i][j + 1:]

    def put_on(self, b, w):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                    if i < 3:
                        self.board[i] = self.board[i][:j] + b + self.board[i][j + 1:]
                    elif i > len(self.board) - 4:
                        self.board[i] = self.board[i][:j] + w + self.board[i][j + 1:]


class Chess(Checker):

    def __init__(self):
        super().__init__(8, "1")

    def put_on(self, a=lambda x: x.lower(), b=lambda x: x):
        self.board[0] = "".join(map(a, "RNBKQBNR"))
        self.board[1] = "".join(map(a, "PPPPPPPP"))
        self.board[-2] = "".join(map(b, "PPPPPPPP"))
        self.board[-1] = "".join(map(b, "RNBKQBNR"))
