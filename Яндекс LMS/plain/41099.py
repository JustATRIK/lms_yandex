import csv

region = input()
start, end = map(lambda x: int(x) - 2015 + 2, input().split())
with open('salary.csv', encoding='utf-8') as inp:
    data = list(filter(lambda x: x[1] == region, list(csv.reader(inp, delimiter=';'))[1:]))
    data = list(filter(lambda x: (int(x[end]) - int(x[start])) / int(x[start]) * 100 < 4, data))
    data = list(map(lambda x: [x[0], x[start], x[end]], data))
    if len(data) > 0:
        with open('out_file.csv', 'w+', encoding='utf-8') as out:
            writer = csv.writer(out, delimiter=';', lineterminator='\n')
            writer.writerow(["Субъект", 2013 + start, 2013 + end])
            writer.writerows(data)
