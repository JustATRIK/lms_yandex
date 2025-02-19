def stars(m, t):
    return f"This is a star of {m} solar masses and {t} K."


def black_hole(m):
    return f"This is black hole of {m} solar masses."


def non_type(t):
    return f"This is an unidentified object of {t} K."


def star_type(m, t=None, determinant=lambda x, y: (x, y)):
    if m != 0 and t is not None:
        m, t = determinant(m, t)
        return stars(m, t)
    if m == 0:
        return non_type(t)
    else:
        return black_hole(m)
        