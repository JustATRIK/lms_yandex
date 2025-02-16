def check_polygon_number(num):
    for n in range(2, num + 1):
        q = (num - n) / ((n - 1) * n / 2) + 2
        if q >= n:
            continue
        if int(q) == q:
            return n, int(q)
    return None, None


def create_polygon_number(n, q):
    return n + (q - 2) * (n * (n - 1)) // 2
