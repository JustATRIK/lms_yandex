def future(*data, **kwargs):
    global VIN
    a = 1
    for i in kwargs.values():
        a *= i
    t = sum(data) * a
    if t > VIN:
        return 'ACCELERATION'
    elif t < VIN:
        return 'DECELERATION'
    return 'UNCHANGED'
