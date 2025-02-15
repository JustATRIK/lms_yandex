import json


def refact(data):
    return [len(data['colors']), data['radius'], (data['x'] ** 2 + data['y'] ** 2) ** 0.5, data['id']]


with open("input.json", "r", encoding="utf-8") as f:
    data = map(refact, json.loads(f.read()))

# print(sorted(data, reverse=True))
print(*map(lambda x: x[-1], sorted(data, reverse=True)))
