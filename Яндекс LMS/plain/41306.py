def mario(a, b):
    if a == 9 or a < b:
        return 0
    if a == b:
        return 1
    return mario(a - 1, b) + (mario(a // 2, b) if a % 2 == 0 else 0)

