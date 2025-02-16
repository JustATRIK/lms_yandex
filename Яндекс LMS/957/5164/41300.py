def degree_indicator(x, p):
    if p == x:
        return 1
    if x > 1:
        return degree_indicator(x / p, p) + 1
    else:
        return degree_indicator(x * p, p) - 1
        