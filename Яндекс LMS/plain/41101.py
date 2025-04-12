import csv
import sys

t = list(map(lambda x: x.strip().split(), sys.stdin.readlines()))
m, n = map(int, t[0])
t = t[1:]
t = filter(lambda x: sum(map(int, (x[2], x[3], x[4]))) >= m and all(map(lambda z: int(z) >= n, (x[2], x[3], x[4]))), t)
t = map(lambda x: x + [sum(map(int, (x[2], x[3], x[4])))], t)
with open('exam.csv', 'w+', encoding='utf-8') as out:
    writer = csv.writer(out, delimiter=';', lineterminator='\n')
    writer.writerow('Фамилия;имя;результат 1;результат 2;результат 3;сумма'.split(';'))
    writer.writerows(t)

