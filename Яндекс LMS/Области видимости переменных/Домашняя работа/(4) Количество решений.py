def solve():
    global n
    a = 0
    for i in range(n + 1):
        for j in range(i, n + 1):
            a += 1
    return a
    