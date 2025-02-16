import datetime


distance, charge_time, avg_speed = int(input()), int(input()), int(input())
departing_at = datetime.datetime.strptime(input(), "%d.%m.%Y %H:%M")
chargers = list(map(int, input().split()))
last_charge = 0
last_charge_at = departing_at
for i in range(1, len(chargers)):
    if chargers[i] - last_charge > distance:
        hours = (chargers[i - 1] - last_charge) / avg_speed
        last_charge_at += datetime.timedelta(hours=hours)
        last_charge = chargers[i - 1]
        print(i, last_charge_at.strftime("%d.%m.%Y %H:%M"))
        last_charge_at += datetime.timedelta(minutes=charge_time)
        