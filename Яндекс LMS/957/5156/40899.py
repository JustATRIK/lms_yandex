def groundhog_day(data):
    res = set()
    targind = 0
    for j in range(1, len(data)):
        for i in range(len(data[0])):
            if data[j - 1][i] != data[j][i]:
                res.add(i)
                targind = j
        if len(res) <= 2:
            res.clear()
            targind = 0
        if targind != 0:
            break
    if len(res) == 0:
        res.add(0)
    return targind, *sorted(list(res))
    