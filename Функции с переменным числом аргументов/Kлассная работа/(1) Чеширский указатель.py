s = input().split()
start, end = s[0].lower(), s[-1].lower()
print(*list(filter(lambda x: start <= x.lower() <= end, s))[1:-1])
