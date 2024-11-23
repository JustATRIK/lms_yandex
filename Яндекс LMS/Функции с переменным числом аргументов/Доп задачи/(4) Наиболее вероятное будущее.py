def best_future(*data):
    res = [-1] * len(data)
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[j] < data[i]:
                res[i] = j
                break
    return res
