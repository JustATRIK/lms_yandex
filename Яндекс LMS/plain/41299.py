def power(x, p):
    if p == 0:
        return 1
    if p > 0:
        return x * power(x, p - 1)
    else:
        return power(x, p + 1) / x
