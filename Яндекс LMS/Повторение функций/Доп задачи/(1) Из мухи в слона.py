import sys


def is_adjacent(a, b):
    if len(a) != len(b):
        return False
    diff = 0
    for c1, c2 in zip(a, b):
        if c1 != c2:
            diff += 1
            if diff > 1:
                return False
    return diff == 1


def find_chain(start, end, middle):
    def backtrack(current, remaining):
        if not remaining:
            if is_adjacent(current[-1], end):
                return current + [end]
            return None
        last_word = current[-1]
        for i in range(len(remaining)):
            word = remaining[i]
            if is_adjacent(last_word, word):
                new_remaining = remaining[:i] + remaining[i + 1:]
                result = backtrack(current + [word], new_remaining)
                if result is not None:
                    return result
        return None

    return backtrack([start], middle)


words = list(map(str.strip, sys.stdin))
start = words[0]
end = words[-1]
middle = words[1:-1]
chain = find_chain(start, end, middle)
if chain:
    print(*chain, sep='\n')
else:
    print(start)
    print(end)
