import json
import csv


res = {}
with open('catalog.csv', 'r', encoding='utf-8') as f:
    reader = list(csv.reader(f, delimiter=';'))
    k = reader[0]
    for pet in reader[1:]:
        if pet[0] not in res:
            res[pet[0]] = {k[1]: {}}
        if pet[1] not in res[pet[0]][k[1]]:
            res[pet[0]][k[1]][pet[1]] = []
        d = {}
        for k1, v in zip(k[2:], pet[2:]):
            d[k1] = v
        res[pet[0]][k[1]][pet[1]].append(d)
with open('pets.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps({"type": res}))
