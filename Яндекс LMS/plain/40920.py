def supercargo_2(load, capacity):
    f = False
    capacity = list(capacity) + [0]
    if capacity[1] == 0:
        f = True
        capacity[1] = -1
    res = []
    for i in load:
        if i > 999:
            res.append(i)
            continue
        if capacity[len(str(i))] == 0 and capacity[len(str(i)) - 1] > 0:
            capacity[len(str(i)) - 1] -= 1
        else:
            res.append(i)
    return tuple(res), sum(capacity) + (1 if f else 0) == 0
