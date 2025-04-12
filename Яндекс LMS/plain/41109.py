import json
from collections import defaultdict


file, category = input(), input()
res = defaultdict(list)
with open(file, "r", encoding="utf-8") as f:
    data = json.loads(f.read())
    for d in data:
        if category in d.keys():
            res[d[category]].append(d["youtuber"])
print(dict(res))
