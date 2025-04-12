import csv
import sys
from collections import defaultdict

t = list(map(lambda x: x.strip().split('\t'), sys.stdin.readlines()))
recipes = defaultdict(lambda: defaultdict(int))
ingredients = set()
for r, i, c in t:
    recipes[r][i] += int(c)
    ingredients.add(i)
ingredients = sorted(list(ingredients))
with open("recipes.csv", "w") as out:
    writer = csv.writer(out, delimiter=";", lineterminator='\n')
    writer.writerow(["recipe"] + ingredients)
    for recipe in sorted(list(recipes.keys())):
        data = [recipe]
        for ingredient in ingredients:
            data.append(recipes[recipe][ingredient])
        writer.writerow(data)
