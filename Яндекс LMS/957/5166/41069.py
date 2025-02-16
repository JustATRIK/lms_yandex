def vaccine_effect(n):
    res = list(filter(lambda x: x[1] >= n, immunoglobulins))
    immunoglobulins.clear()
    immunoglobulins.extend(res)
