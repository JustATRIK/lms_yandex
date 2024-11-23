def integers_only(data):
    data1 = []
    for i in data:
        if type(i) is int:
            data1.append(i)

    return sorted(data1)
