import sys


n = int(input())
for i in map(str.strip, sys.stdin):
    s = n % len(i)
    print(i[s:] + i[:s])
