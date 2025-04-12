import csv


def messier_search(targ):
    with open('messier.csv', encoding='utf-8') as inp:
        data = list(csv.reader(inp, delimiter=';'))
        t = data[0].index(targ)
        data = data[1:]
        res = set(filter(lambda x: x != '', map(lambda x: x[t], data)))
        return sorted(list(res))
    