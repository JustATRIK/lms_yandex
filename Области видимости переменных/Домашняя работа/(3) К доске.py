log = []
b = set()


def pupil_number(surname):
    global log
    print(log.index(surname) + 1 if surname in log else "������ ������� ���.")


def add_pupil(surname):
    global log
    if surname not in log:
        log.append(surname)
        print(f"������ {surname} ��������.")
    else:
        print("����� ������ ��� ���� � �������.")
    log.sort()


def to_the_blackboard(n):
    global log, b
    n -= 1
    if log[n] in b:
        print("��� �����, �� ���� ��� ��������!")
    else:
        print(f"{log[n]}, � �����!")
        b.add(log[n])
