import datetime


def days_left(date):
    date = list(map(int, date.split('.')))
    date = datetime.date(date[-1], date[1], date[0])
    return (date - datetime.date.today()).days
