def selection(data, condition):
    a = []
    for i in data:
        if i % condition == 0:
            a.append(i)
    return a
    