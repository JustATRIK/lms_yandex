def jogging(a, speed=None, reduce=None, kkal=None):
    total = (a * 60 * speed) // 1000 * kkal
    return total, total >= reduce
