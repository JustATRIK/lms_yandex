d = {"B": 1, "KB": 1024, "MB": 1024 ** 2, "GB": 1024 ** 3}


def to_bytes(n, v):
    return n * d[v]


def in_largest_units(n):
    for k, v in reversed(d.items()):
        res = n // v
        if res == 0:
            continue
        return f'{round(n / v)} {k}'
