import sys

for i in map(str.strip, sys.stdin):
    if len(list(filter(lambda x: "0" in x, i.split()))) > len(i.split()) // 2:
        print("ALUMINUM CUCUMBERS")
        exit()
print("EVERGREEN TOMATOES")

