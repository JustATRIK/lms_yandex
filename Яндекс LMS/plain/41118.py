import json
from collections import defaultdict


with open('input.txt', 'r', encoding='utf-8') as f:
    inp = f.readlines()
    cn = defaultdict(int)
    for w in inp:
        cn[w[0]] += 1
    res = {}
    for k, v in cn.items():
        res[k] = round(v / len(inp) * 100, 2)

    with open('output.json', 'w', encoding='utf-8') as out:
        out.write(json.dumps(res))
