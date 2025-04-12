def circuit_resistance(*a, connection='serial', conductivity=False):
    if connection == 'serial':
        res = sum(a)
    else:
        res = 1 / sum(map(lambda x: 1 / x, a))
    return res if not conductivity else 1 / res
