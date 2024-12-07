import sys

a = list(map(lambda x: x.strip().split(), sys.stdin))
temp = float(a[-1][0]) + (273.15 if a[-1][1] == "C" else 0)
print(*set(map(lambda x: x[0],
               filter(lambda x: float(x[1]) + (273.15 if x[2] == "C" else 0) < temp, a[:-1]))), sep='\n')
