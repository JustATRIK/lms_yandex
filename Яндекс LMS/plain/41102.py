import csv

a = []
with open("yndx_share_price.csv", encoding="utf-8") as ppp:
    data = list(map(lambda x: x[-1], list(csv.reader(ppp, delimiter=","))[1:]))
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] < data[j]:
                a.append(str(j - i))
                break
        else:
            a.append('0')
open('predict.txt', 'w+').write(" ".join(a))
