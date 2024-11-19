def anthropic_principle(*data, k=2):
    result = []
    for i in range(min(data) + 1, max(data)):
        res = tuple(sorted([j for j in range(2, i // 2 + 1) if i % j == 0 and i not in data]))
        if len(res) == k:
            result.append(res)
    return result
