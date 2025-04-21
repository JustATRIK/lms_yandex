class Scrabble:

    _letter_scores = {
        "A": 1, "E": 1, "I": 1, "L": 1, "N": 1, "O": 1, "R": 1, "S": 1, "T": 1, "U": 1,
        "D": 2, "G": 2,
        "B": 3, "C": 3, "M": 3, "P": 3,
        "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
        "K": 5,
        "J": 8, "X": 8,
        "Q": 10, "Z": 10
    }

    def __init__(self, letters):
        self.letters = letters.upper()
        self.letters_count = {}
        for letter in self.letters:
            self.letters_count[letter] = self.letters_count.get(letter, 0) + 1

    def __call__(self, word):
        word = word.upper()
        temp_count = self.letters_count.copy()
        score = 0
        for letter in word:
            if temp_count.get(letter, 0) <= 0:
                return 0
            temp_count[letter] -= 1
            score += self._letter_scores.get(letter, 0)
        return score

    def total_score(self):
        return sum(self._letter_scores.get(letter, 0) for letter in self.letters)

    def __lt__(self, other):
        if self.total_score() != other.total_score():
            return self.total_score() < other.total_score()
        return len(self.letters) < len(other.letters)

    def __le__(self, other):
        if self.total_score() != other.total_score():
            return self.total_score() <= other.total_score()
        return len(self.letters) <= len(other.letters)

    def __eq__(self, other):
        return self.total_score() == other.total_score() and len(self.letters) == len(other.letters)

    def __ne__(self, other):
        return not (self == other)

    def __gt__(self, other):
        if self.total_score() != other.total_score():
            return self.total_score() > other.total_score()
        return len(self.letters) > len(other.letters)

    def __ge__(self, other):
        if self.total_score() != other.total_score():
            return self.total_score() >= other.total_score()
        return len(self.letters) >= len(other.letters)

    def __str__(self):
        return f"Scrabble('{self.letters}')"
