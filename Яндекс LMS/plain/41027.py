import sys

print(min(map(str.strip, sys.stdin), key=lambda x: (sum(map(int, list(x))), -len(x), int(x))))
