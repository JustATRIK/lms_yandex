a = int(input())
for i in range(7, -1, -1):
    print(((1 << i) & a) >> i, end='')