d = {}


def diversity(data):
    if data in d:
        d[data] += 1
    else:
        d[data] = 1
    return d[data]
