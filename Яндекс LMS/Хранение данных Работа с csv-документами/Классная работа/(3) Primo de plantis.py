import csv
import sys

t = list(map(lambda x: x.strip().split("\t"), sys.stdin.readlines()))
with open('plantis.csv', 'w+', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';', lineterminator='\n')
    writer.writerow("nomen;definitio;pluma;Russian nomen;familia;Russian nomen familia".split(";"))
    writer.writerows(t)
