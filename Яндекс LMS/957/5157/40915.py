def blade(a):
    return [a[:len(a) - i] if len(a) % 2 == 0 else a[i:] for i in range(len(a))]
