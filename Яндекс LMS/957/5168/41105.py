import csv

with open("posters.csv", encoding="utf-8") as f:
    data = list(csv.reader(f, delimiter=";"))
    ind = tuple(map(lambda x: data[0].index(x), map(str.strip, open('in_file.txt').readlines())))
    data = map(lambda x: [int(x[0]), x[1], int(x[2]), int(x[3]), int(x[4]), x[5]], data[1:])
    data = sorted(data, key=lambda x: tuple(map(lambda y: x[y], ind)))
    with open("sorted.csv", 'w+', encoding="utf-8") as out:
        writer = csv.writer(out, delimiter=';', lineterminator='\n')
        writer.writerows(data)
