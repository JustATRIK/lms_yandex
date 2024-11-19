def supercargo_2(load, capacity):
    capacity = list(capacity) + [0]
    res = []
    for i in load:
        if i > 999:
            res.append(i)
            continue
        print(len(str(i)) - 1, capacity)
        if capacity[len(str(i))] == 0 and capacity[len(str(i)) - 1] > 0:
            capacity[len(str(i)) - 1] -= 1
        else:
            res.append(i)
    return tuple(res), sum(capacity) == 0
