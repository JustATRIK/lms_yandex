def positions(a):
    typee = type(a)
    if typee in [list, set, tuple]:
        return max(a) if len(a) > 0 else None
    elif typee == int:
        return a + (2 if a % 2 == 0 else 1)
    elif typee == str:
        print(len(a))
    return None
