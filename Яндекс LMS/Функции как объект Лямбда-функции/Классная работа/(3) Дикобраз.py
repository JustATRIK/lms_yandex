def porcupine(*data):
    a = sum(map(lambda x: x[0], data)) / len(data)
    b = sum(map(lambda x: x[1], data)) / len(data)
    return sorted(list(filter(lambda x: x[1] < b and x[0] > a, data)))
