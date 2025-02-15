import datetime
import math

price, sale, time1, deliv, time2 = int(input()), int(input()), int(input()), list(map(int, input().split('.'))), list(
    map(int, input().split(':')))

time = datetime.datetime(deliv[-1], deliv[1], deliv[0], time2[0], time2[1])
deliv_date = time.date() + datetime.timedelta(time1)
if datetime.time(6, 0, 0) < time.time() < datetime.time(12, 30):
    if time.weekday() != 0:
        deliv_date -= datetime.timedelta(1)
    price -= math.ceil(price / 100 * sale)

print(f'{deliv_date.strftime("%d-%m-%Y")} {price}')
