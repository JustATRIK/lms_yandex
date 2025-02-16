def catch_flies(*data, func=None):
    data = list(map(lambda x: (x['x'], x['y']), data))
    if func:
        data = list(filter(lambda x: func(x[0], x[1]), data))
    min_x, max_x = int(10e9), 0
    min_y, max_y = int(10e9), 0
    for x, y in data:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    return [{'x': min_x, 'y': max_y}, {'x': max_x, 'y': min_y}]
