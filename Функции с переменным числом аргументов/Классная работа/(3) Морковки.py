def carrots(n, m, *carrots):
    for i in range(len(carrots) - n):
        if sum(carrots[i:i + n]) == m:
            return i + 1
    return 0

