import json
from collections import defaultdict


with open('russian_words.txt', 'r', encoding='utf-8') as f:
    inp = f.readlines()
    res = defaultdict(list)
    for w in inp:
        res[w[0]].append(w.strip())
    with open('russian_words.json', 'w', encoding='utf-8') as out:
        json.dump(res, out, ensure_ascii=False)
