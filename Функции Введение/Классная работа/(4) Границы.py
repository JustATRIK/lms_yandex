def borders(a, b, c):
    minn_y = min(a[1], b[1])
    maxx_y = max(a[1], b[1])
    minn_x = min(a[0], b[0])
    maxx_x = max(a[0], b[0])
    if (((a[0] == c[0] or b[0] == c[0]) and c[1] in range(minn_y, maxx_y))
            or ((a[1] == c[1] or a[1] == c[1]) and c[0] in range(minn_x, maxx_x))):
        print("AT THE EDGE")
    elif c[0] in range(minn_x + 1, maxx_x) and c[1] in range(minn_y + 1, maxx_y):
        print("INSIDE")
    else:
        print("OUTSIDE")
