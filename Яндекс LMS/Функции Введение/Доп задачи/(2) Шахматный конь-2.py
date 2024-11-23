b = 'abcdefgh'


def horse2(a):
    coords = (b.index(a[0]), int(a[1]) - 1)
    for j in range(1, 3):
        for i in range(4):
            if i == 0:
                xp, yp = -1, -1
            elif i == 1:
                xp, yp = -1, 1
            elif i == 2:
                xp, yp = 1, -1
            else:
                xp, yp = 1, 1

            x = coords[0] + j * xp
            y = coords[1] + (3 - j) * yp
            if -1 < x < 8 and -1 < y < 8:
                print(b[x] + str(y + 1))
