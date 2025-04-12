def express(*data):
    return list(filter(lambda x: not (len(x) < 8 or len(x) == len(set(x))
                                      or len(set(x) & set("02468")) > 0 or (data.index(x) + 1) % 7 == 0), data))
    