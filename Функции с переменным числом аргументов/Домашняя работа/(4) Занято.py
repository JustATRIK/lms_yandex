def sequence_occupied(**data):
    for k, v in zip(data.keys(), data.values()):
        for j in v:
            places[int(k) - 1][j - 1] = 1
    maxx = 0
    a = 0
    for i in places:
        curr = 0
        for j in i:
            if j == 1:
                curr += 1
            else:
                curr = 0
            if maxx < curr:
                maxx, a = curr, places.index(i) + 1
    return maxx, a

# places = []
