def vaccine_filter(n):
    res = list(filter(n, immunoglobulins))
    immunoglobulins.clear()
    immunoglobulins.extend(res)
