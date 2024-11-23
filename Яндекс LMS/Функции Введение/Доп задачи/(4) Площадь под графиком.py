def square(data):
    s = 0
    for data1 in data:
        s += (data1[0] + data1[1]) / 2 * data1[2]
    print(s)
