import csv
from collections import defaultdict

with open("in_file.csv", encoding="utf-8") as f:
    data = list(csv.reader(f, delimiter=";"))
    files = defaultdict(set)
    for p, c in data:
        files[p].add(c)
    parent = ""
    for p in files.keys():
        f = True
        for j in files.keys() - {p}:
            if p in files[j]:
                f = False
                break
        if f:
            parent = p
            break
    q = [[parent]]
    level = 0
    levels = defaultdict(set)
    while q:
        p = q.pop()
        n = []
        for c in p:
            levels[level].add(c)
            n += list(files[c])
        if n:
            q.append(n)
        level += 1
    with open('out_file.csv', 'w') as out:
        for i in range(max(levels.keys()) + 1):
            out.write(";".join(sorted(list(levels[i]))) + "\n")
