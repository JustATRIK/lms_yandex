def lines_intersection(xy1, xy2, xy3, xy4):
    k1 = (xy1[1] - xy2[1]) / (xy1[0] - xy2[0])
    b1 = xy1[1] - xy1[0] * k1
    k2 = (xy3[1] - xy4[1]) / (xy3[0] - xy4[0])
    b2 = xy3[1] - xy3[0] * k2
    if k1 == k2:
        return None, None
    x = (b2 - b1) / (k1 - k2)
    return x, b1 * x + k1
    