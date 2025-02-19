from math import factorial


def calc_n_sin(x, n):
    return (x ** (2 * n + 1) / factorial(2 * n + 1)) * (-1) ** n


def calc_n_cos(x, n):
    return (x ** (2 * n) / factorial(2 * n)) * (-1) ** n


def trigonometric_function(mode, x, n):
    res = 0
    for i in range(n + 1):
        if mode == 'sin':
            res += calc_n_sin(x, i)
        else:
            res += calc_n_cos(x, i)
    return res
