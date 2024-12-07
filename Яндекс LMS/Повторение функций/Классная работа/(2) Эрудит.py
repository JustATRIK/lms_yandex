import sys


def check(s1, s2):
    if len(s1) >= len(s2):
        return False
    s2 = list(s2)
    for i in s1:
        if i not in s2:
            return False
        s2.remove(i)
    return True


for i in map(lambda x: x.strip().split(), sys.stdin):
    print(*sorted(list(filter(lambda x: check(x, i[0]), i[1:])), key=len, reverse=True))
    