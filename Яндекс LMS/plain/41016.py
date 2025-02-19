def hologram(*data, transformation=1):
    if transformation == 1:
        return list(map(lambda x: x.title(), data))
    elif transformation == 2:
        return list(map(lambda x: "".join([x[i] for i in range(0, len(x), 2)]), data))
    elif transformation == 3:
        return list(map(len, data))
    else:
        return list(map(lambda x: x if len(x) % 2 == 0 else "".join(sorted(list(set(x)))), data))
        