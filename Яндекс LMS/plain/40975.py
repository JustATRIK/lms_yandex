def quarters(*data):
    data = list(filter(lambda x: x[0] != 0 and x[1] != 0, data))
    return {
        'I': len(list(filter(lambda x: x[0] > 0 and x[1] > 0, data))),
        'II': len(list(filter(lambda x: x[0] < 0 < x[1], data))),
        'III': len(list(filter(lambda x: x[0] < 0 and x[1] < 0, data))),
        'IV': len(list(filter(lambda x: x[0] > 0 > x[1], data))),
    }
