def allocation(data):
    a = []
    for i in data:
        if places[i[0] - 1][i[1] - 1] == 1:
            a.append(i)
        places[i[0] - 1][i[1] - 1] = 1
    return a

# places = []
