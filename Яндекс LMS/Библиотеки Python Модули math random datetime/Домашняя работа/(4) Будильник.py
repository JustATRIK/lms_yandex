import datetime


def alarm(day, interval=10):
    day = list(map(int, day.split('-')))
    day = datetime.date(*day)
    start = datetime.date(2021, 1, 4)
    days = (day - start).days
    week = days // 7
    res = []
    if week % 2 != 1:
        if day.weekday() == 3:
            res = [(datetime.datetime(1900, 1, 1, 7, 45))]
        elif day.weekday() < 5:
            res = [(datetime.datetime(1900, 1, 1, 8, 30))]
        else:
            res = [(datetime.datetime(1900, 1, 1, 10, 00))]
    else:
        if day.weekday() == 3 or day.weekday() == 2:
            res = [(datetime.datetime(1900, 1, 1, 9, 30))]
        elif day.weekday() < 5:
            res = [(datetime.datetime(1900, 1, 1, 9, 00))]
        else:
            res = [(datetime.datetime(1900, 1, 1, 11, 00))]
    if day.weekday() < 5:
        res.append(res[0] + datetime.timedelta(minutes=interval))
    return tuple(map(lambda x: x.strftime("%H:%M"), res))
