def line(x1, y1, x2, y2):
    k = (y1 - y2) / (x1 - x2)
    b = y1 - x1 * k
    print(f'y = {round(k, 2)} * x {"-" if b < 0 else "+"} {abs(round(b, 2))}')
