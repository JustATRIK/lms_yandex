import sys

print(max(map(str.strip, sys.stdin), key=lambda x: (x.count("a"), len(x), x)))
