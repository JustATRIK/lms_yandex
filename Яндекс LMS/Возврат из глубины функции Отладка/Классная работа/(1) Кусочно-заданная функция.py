def definition(x):
    if x <= 0:
        return x ** 2 + 2 * x
    elif x <= 2:
        return x
    elif x <= 4:
        return 4
    else:
        return 8 / x
