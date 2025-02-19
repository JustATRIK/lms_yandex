def opinions(*data):
    d = {}
    for i in data:
        for k, v in zip(i.keys(), i.values()):
            d.setdefault(k, set()).add(v)
    return d
