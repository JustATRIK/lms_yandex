def check_polygon_number(num):
    for i in range(num):
        for j in range(num):
            if create_polygon_number(i, j) == num:
                return i, j
    return None, None


def create_polygon_number(n, q):
    return n + (q - 2) * (n * (n - 1)) // 2

