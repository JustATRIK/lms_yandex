x, y = map(int, input().split())
print(*sorted(
    map(lambda z: (z[2] / ((x - z[0]) ** 2 + (y - z[1]) ** 2), ((x - z[0]) ** 2 + (y - z[1]) ** 2), z[0], z[1]),
        [tuple(map(int, input().split())) for i in range(int(input()))]), key=lambda z: (z[0], -z[1]))[-1][2:])
