from collections import defaultdict

a = input()
res = defaultdict(str)
for i in a.split("! "):
    res[len(list(filter(lambda x: x in "аяоёуюэеиы", list(i))))] += (i + "\n")
print(*filter(lambda x: x.count('\n') > 1, map(lambda x: res[x], sorted(res.keys(), reverse=True))), sep='\n')
