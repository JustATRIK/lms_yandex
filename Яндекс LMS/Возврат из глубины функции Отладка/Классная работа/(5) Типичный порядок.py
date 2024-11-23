def positions(a):
    typee = type(a)
    if typee in [list, set, tuple]:
        return max(a) if len(a) > 0 else None
    elif typee in [float, int]:
        return int(a) + (2 if int(a) % 2 == 0 else 1)
    elif typee == str:
        return len(a)
    return None
