mid = 0


def changing_the_norm(data):
    global mid
    res = 0
    for i in data:
        if i > mid:
            res += 1
    mid = sum(data) / len(data)
    return res
