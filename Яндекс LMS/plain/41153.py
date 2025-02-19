import datetime


def asteroid_angle(n):
    return round((360 * ((datetime.date.today() - datetime.date(2000, 1, 1)).days % n)) / n)
