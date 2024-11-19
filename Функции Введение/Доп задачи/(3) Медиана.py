def median(a):
    a.sort()
    if len(a) == 0:
        print(0)
    if len(a) % 2 == 0:
        lebb = len(a) // 2
        print((a[lebb] + a[lebb + 1]) / 2)
    else:
        print(a[len(a) // 2])
