def warmer_day(temperature1):
    temperature = []
    for i in temperature1:
        for j in i:
            temperature.append(j)
    mid = sum(temperature) / len(temperature)
    for i in range(len(temperature)):
        if temperature[i] > mid:
            return i + 1
    return None
