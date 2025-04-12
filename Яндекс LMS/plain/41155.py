import math


a, b, c, sc = [float(input()) for _ in range(4)]
d = c / sc
print(math.degrees(math.asin(a / d)), math.degrees(math.asin(b / d)), sep='\n')
