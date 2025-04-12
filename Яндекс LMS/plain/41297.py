def func(n):
    if n == 0:
        return 0
    if n > 0 and n % 3 == 0:
        return func(n / 3) + 1
    else:
        return func(n - 1) + 2
