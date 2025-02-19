import csv

t = int(input())
with open('vps.csv', encoding='utf-8') as f:
    reader = list(csv.reader(f, delimiter=';'))[1:]
    print(*map(lambda x: x[0], list(filter(lambda x: int(x[-2]) >= t, reader))), sep='\n')