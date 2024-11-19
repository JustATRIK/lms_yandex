d = {}


def total(datas):
    global d
    for data in datas:
        key = " ".join(data.split(" ")[:-1])
        if key in d:
            d[key] = (d[key][0] + 1, d[key][1] + float(data.split(" ")[-1]))
        else:
            d[key] = (1, float(data.split(" ")[-1]))
    total = 0
    for key, value in zip(d.keys(), d.values()):
        total += value[1]
        print(f"{key} - {value[0]} - {round(value[1], 1)} kCal")
    print("------", f"Total: {round(total, 1)} kCal\n")
