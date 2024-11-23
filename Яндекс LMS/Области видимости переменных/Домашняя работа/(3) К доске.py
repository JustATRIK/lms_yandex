log = []
b = set()


def pupil_number(surname):
    global log
    print(log.index(surname) + 1 if surname in log else "Такого ученика нет.")


def add_pupil(surname):
    global log
    if surname not in log:
        log.append(surname)
        print(f"Ученик {surname} добавлен.")
    else:
        print("Такой ученик уже есть в журнале.")
    log.sort()


def to_the_blackboard(n):
    global log, b
    n -= 1
    if log[n] in b:
        print("Сан Саныч, Вы меня уже вызывали!")
    else:
        print(f"{log[n]}, к доске!")
        b.add(log[n])
