import sys

print("FAIL" if all(any(int(j) % 5 == 0 for j in i.split("; ")) for i in map(str.strip, sys.stdin)) else "OK")
