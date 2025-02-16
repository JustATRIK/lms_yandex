def typification(data):
    d = {}
    for i in data:
        if type(i).__name__ in d:
            d[type(i).__name__].append(i)
        else:
            d[type(i).__name__] = [i]
    return d
