from math import sqrt, sin, radians

g = 9.8


def collect_stones():
    global L, g
    L += 0.5
    return sqrt(((L - 0.5) * g) / sin(2 * radians(ALPHA)))
