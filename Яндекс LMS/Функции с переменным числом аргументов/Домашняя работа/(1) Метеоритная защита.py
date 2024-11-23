def defense(*data):
    max_width, max_height = 0, 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            max_width = max(max_width, int(((data[i][0] - data[j][0]) ** 2) ** 0.5))
            max_height = max(max_height, int(((data[i][1] - data[j][1]) ** 2) ** 0.5))
    return max_width, max_height
