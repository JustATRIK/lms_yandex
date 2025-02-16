def min_in_column(arr, n):
    minn = 100000000
    for i in arr:
        minn = min(minn, i[n])
    return minn


def scare_crows(original):
    copyy = []
    for i in original:
        copyy.append(i.copy())
    for i in range(len(original)):
        for j in range(len(original[0])):
            copyy[i][j] = min(min_in_column(original, j), min(original[i]))
    return copyy
