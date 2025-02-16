import csv

with open("posters.csv", encoding="utf-8") as f:
    data = list(csv.reader(f, delimiter=";"))
    ind = data[0].index(open('in_file.txt').readline().strip())
    data = map(lambda x: [int(x[0]), x[1], int(x[2]), int(x[3]), int(x[4]), x[5]], data[1:])
    data = sorted(data, key=lambda x: x[ind])
    with open("sorted.csv", 'w+', encoding="utf-8") as out:
        writer = csv.writer(out, delimiter=';', lineterminator='\n')
        writer.writerows(data)
