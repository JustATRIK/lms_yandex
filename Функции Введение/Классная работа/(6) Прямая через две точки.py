def line(x1, y1, x2, y2):
    print(f'y = {round((y1 - y2) / (x1 - x2), 2)} * x {"-" if y1 + y2 < 0 else "+"} {float(abs(y1 + y2))}')
    