def haystack(*data, needle=None):
    if len(data) == 0:
        return -1
    if data[0] == needle:
        return 0
    res = haystack(*data[1:], needle=needle)
    return res + 1 if res != -1 else -1
