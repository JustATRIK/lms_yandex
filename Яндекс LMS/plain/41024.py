def trend(*data, **functions):
    for name, func in zip(functions.keys(), functions.values()):
        if all(map(lambda x: abs(func(x[0]) - x[1]) <= 0.01, data)):
            return name
    return None
