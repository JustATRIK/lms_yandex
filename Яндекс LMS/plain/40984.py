def anthropic_principle(*data, k=2):
    result = []
    for i in range(min(data) + 1, max(data)):
        res = []
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0 and i not in data:
                res.append(j)
                if i // j not in data and i // j != j:
                    res.append(i // j)
        if len(res) == k:
            result.append(tuple(sorted(res)))
    return result
