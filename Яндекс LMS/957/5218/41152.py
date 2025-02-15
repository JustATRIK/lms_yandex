import random


def generate_fandom(n, names):
    res = []
    distances = list(range(100, 501))
    for i in range(n):
        distance = random.choice(distances)
        distances.remove(distance)
        name = random.choice(names)
        names.remove(name)
        res.append((name, random.randint(10, 20), random.randint(1, 100) * 10000, distance))
    return res
