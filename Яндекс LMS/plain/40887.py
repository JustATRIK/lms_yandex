alphabet = 'abcdefgh'


def horse(a, b):
    coords_1 = (alphabet.index(a[0]), int(a[1]))
    coords_2 = (alphabet.index(b[0]), int(b[1]))
    print(((abs(coords_1[0] - coords_2[0]) == 2 and abs(coords_1[1] - coords_2[1]) == 1) or
           (abs(coords_1[0] - coords_2[0]) == 1 and abs(coords_1[1] - coords_2[1]) == 2)))
