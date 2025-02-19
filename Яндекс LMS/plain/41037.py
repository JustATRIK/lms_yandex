import sys
from collections import defaultdict

res = defaultdict(int)
for a in map(str.strip, sys.stdin):
    s = a.find("AUG") + 3
    if s != 2:
        e = list(filter(lambda x: x != -1, [a.find("UAA", s), a.find("UGA", s), a.find("UAG", s)]))
        if not e:
            e = [len(a)]
        for i in range(s, min(e) - 2, 3):
            c = a[i:i + 3]
            if len(c) != 3:
                continue
            res[c] += 1
ress = list(map(lambda x: f'{x}: {res[x]}', sorted(res.keys(), key=lambda x: (res[x], x), reverse=True)))
print(*ress[:min(10, len(ress))], sep='\n')