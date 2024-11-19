def supercargo(load, capacity):
    d = {}
    for i in load:
        if len(str(i)) in d:
            d[len(str(i))].append(i)
        else:
            d[len(str(i))] = [i]
    res = []
    for i in range(len(d)):
        if i >= 3:
            res += d[i + 1]
            continue
        if (i + 1) in d:
            res += d[i + 1][min(len(d[i + 1]), capacity[i]):]
    return tuple(res), len(res) != 0
