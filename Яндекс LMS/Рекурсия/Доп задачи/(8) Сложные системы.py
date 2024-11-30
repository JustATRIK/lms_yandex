def complex_systems(arr):
    if not (type(arr) is list):
        return arr
    res = []
    for i in arr:
        res1 = complex_systems(i)
        if not (type(res1) is list):
            res.append(res1)
        else:
            res += res1
    return res