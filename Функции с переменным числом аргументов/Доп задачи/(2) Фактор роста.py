def nutrient_medium(portions, *data, periods=1, mult=1):
    result = [max(0, round((portions // len(data) + (1 if i < portions % len(data) else 0)) * (data[i] * mult)
                           ** periods, 3)) for i in range(len(data))]
    return sum(result), result
