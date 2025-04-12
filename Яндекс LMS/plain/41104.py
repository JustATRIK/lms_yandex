import csv

with open("alpha_oriona.csv", encoding="utf-8") as f:
    data = list(map(lambda x: [x[0], x[1], int(x[2]), x[3]], list(csv.reader(f, delimiter=";"))[1:]))
    c = data[-1].copy()
    c[-2] += 1
    data.append(c)
    res, tmp, s, e = 0, 1, '', ''
    for i in range(1, len(data)):
        if int(data[i][-2]) <= int(data[i - 1][-2]):
            tmp += 1
            if tmp == 2:
                s = data[i - 1][0] + " " + data[i - 1][1]
        else:
            if tmp > res:
                res = tmp
                e = s
            tmp = 1
    with open("result.txt", "w") as out:
        out.write(f'{res}\n{e}')
