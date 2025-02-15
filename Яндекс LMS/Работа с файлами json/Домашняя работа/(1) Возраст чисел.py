import json
import sys
from collections import defaultdict


def age(num):
    num = int(num)
    if num < 10:
        return 1
    age = 0
    while num > 9:
        res = 1
        for i in str(num):
            res *= int(i)
        num = res
        age += 1
    return age


t = list(map(str.strip, sys.stdin.readlines()))
res = defaultdict(list)
for i in t:
    res[age(i)].append(i)
with open('numbers_age.json', 'w', encoding='utf-8') as out:
    out.write(json.dumps(res))