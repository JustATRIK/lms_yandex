from collections import defaultdict

a = list(filter(lambda x: len(x) == 3 or len(x) == 2, map(lambda x: x.upper(), input().split())))
d = defaultdict(int)
for i in a:
    d[i] += 1
print(dict(d))
