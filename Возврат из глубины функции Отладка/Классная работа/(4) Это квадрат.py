def is_it_square(*args):
    a = set()
    for i in range(4):
        for j in range(i + 1, 4):
            a.add(((args[i][0] - args[j][0]) ** 2 + (args[i][1] - args[j][1]) ** 2) ** 0.5)
    if len(a) == 2:
        return min(a)
    return None
