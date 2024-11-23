def supercargo(load, capacity):
    capacity = list(capacity)
    d = {1: [], 2: [], 3: []}
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
            capacity[i] -= min(len(d[i + 1]), capacity[i])
    return tuple(res), sum(capacity) == 0
