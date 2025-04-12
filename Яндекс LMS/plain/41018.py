a = input().split("; ")
a = list(map(lambda x: x.split()[-1], list(filter(lambda x: " " in x, a))))
print(", ".join(map(lambda x: x[:len(x) - 3] + "lone" if x.endswith("ino") else x[:len(x) - 2] + "ino", a)))