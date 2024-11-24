a, b = map(int, input().split())
print(1 << abs(a) | 1 << abs(b))