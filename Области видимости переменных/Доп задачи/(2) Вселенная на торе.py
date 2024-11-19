def get(i, j, arr):
    if i < 0:
        i += len(arr)
    elif i >= len(arr):
        i %= len(arr)
    if j < 0:
        j += len(arr[0])
    elif j >= len(arr[0]):
        j %= len(arr[0])
    return arr[i][j]


def research_universe(arr, key=None):
    if key is None:
        return None
    a = [[0] * len(arr[0]) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            c = 0
            c += 1 if key(get(i - 1, j - 1, arr)) else 0
            c += 1 if key(get(i, j - 1, arr)) else 0
            c += 1 if key(get(i - 1, j, arr)) else 0
            c += 1 if key(get(i + 1, j - 1, arr)) else 0
            c += 1 if key(get(i + 1, j, arr)) else 0
            c += 1 if key(get(i - 1, j + 1, arr)) else 0
            c += 1 if key(get(i, j + 1, arr)) else 0
            c += 1 if key(get(i + 1, j + 1, arr)) else 0
            a[i][j] = c
    return a
