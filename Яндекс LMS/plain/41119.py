import csv
import json


location = open('state.txt', 'r', encoding='utf-8').read().strip()
with open('world_university_ranking.csv', 'r', encoding='utf-8') as f:
    inp = list(csv.reader(f, delimiter=','))[1:]
    res = []
    for r, i, l, s in list(filter(lambda x: len(x) > 0 and x[2] == location, inp)):
        res.append({'institution': i, 'rank': r, 'ar score': s})

    with open('state.json', 'w', encoding='utf-8') as out:
        out.write(json.dumps(res))
