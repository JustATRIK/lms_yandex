from collections import defaultdict

a, n = [], input()
while n != "":
    b, d1 = list(map(int, n.split())), defaultdict(int)
    for p in b:
        d1[abs(p)] += 1 * (-1 if p < 0 else 1)
    if all(map(lambda x: list(d1.values())[0] == x, d1.values())) and (len(d1) == 3 or list(d1.values())[0] == 0):
        a.append(" ".join(map(str, b)))
    n = input()
print(*sorted(a, key=len), sep='\n')
