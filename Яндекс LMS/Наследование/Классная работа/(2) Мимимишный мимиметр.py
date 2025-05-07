from collections import defaultdict


class Liked:
    _emojis = [":)", ":(", ";)", ";(", "(", ")"]

    def __init__(self, *lines):
        self.lines = list(lines)

    def likes(self):
        counts = defaultdict(int)
        for line in self.lines:
            for emoji in self._emojis:
                if line.count(emoji) > 0:
                    counts[emoji] += line.count(emoji)
                    line = line.replace(emoji, "")
        return dict(counts)


class MiMiMi(Liked):

    def __init__(self, *lines):
        super().__init__(*lines)
        self.lines = list(filter(lambda x: "cat" in x or "kitten" in x, lines))
