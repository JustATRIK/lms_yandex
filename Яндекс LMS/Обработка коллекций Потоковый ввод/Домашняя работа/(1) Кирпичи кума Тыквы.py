a, b = map(int, input().split())
print(*(sorted(list(filter(lambda x: x % 6 == 0, range(a, b + 1))), key=lambda x: -x) + sorted(
    list(filter(lambda x: x % 3 == 0 and x % 2 == 1, range(a, b + 1))), key=lambda x: -x)))
