import json
import csv


res = []
with open('dragons.csv', 'r', encoding='utf-8') as f:
    reader = list(csv.reader(f, delimiter=','))
    for dragon in reader[1:]:
        d = {}
        for k, v in zip(reader[0], dragon):
            d[k] = v
        res.append(d)
with open('dragons.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps({"dragons": res}))
