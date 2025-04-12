from math import degrees


deg = degrees(float(input()))
print(deg - (deg // 360) * 360 if deg >= 360 else deg)
