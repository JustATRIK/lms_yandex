import csv

t = list(map(lambda x: x.strip().split("\t"), open('messier.txt', 'r').readlines()))
with open('messier.csv', 'w+', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';', lineterminator='\n')
    writer.writerows(t)
