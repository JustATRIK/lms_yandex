import math


a = float(input()) * 1000
b = int(a) % 10
if b >= 5 and int(a):
    a += 10
a -= b
print(math.floor(a) / 1000)
