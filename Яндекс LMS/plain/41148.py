import random
from string import ascii_lowercase, digits


def name(lenn):
    res = random.choice(ascii_lowercase) + random.choice(digits) + " "
    used = {res[0]}
    res += random.choice(sorted(list(set(ascii_lowercase) - used))[:11]).upper()
    used.add(res[-1].lower())
    for i in range(lenn - 4):
        res += random.choice(tuple(set(ascii_lowercase) - used))
        used.add(res[-1])
    return res
    