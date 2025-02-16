def smart_search(*data, func=lambda x: x):
    if type(data[0]) is str:
        return tuple(filter(lambda x: x[0].isupper(), data))
    else:
        return tuple(filter(func, data))
        