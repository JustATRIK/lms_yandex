from math import cos, radians


def latitude(phi):
    print(round(cos(radians(phi)) * 6370))
