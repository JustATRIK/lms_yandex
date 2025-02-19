def gears(data1, n, m):
    data = []
    for i in data1:
        for j in i:
            data.append(j)
    for i in range(len(data)):
        for j in range(i, len(data)):
            if data[j] != 0 and data[i] / data[j] == n / m:
                return data[i], data[j]
            elif data[i] != 0 and data[j] / data[i] == n / m:
                return data[j], data[i]
    return None, None
