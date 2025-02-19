def accumulation(*args):
    a = [0] * (len(args) + 1)
    for i in range(1, len(args) + 1):
        a[i] = a[i - 1] + args[i - 1]
    return a
