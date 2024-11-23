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
    for key in sorted(d):
        total += d[key][1]
        print(f"{key} - {d[key][0]} - {round(d[key][1], 1)} kCal")
    print(f"------\nTotal: {round(total, 1)} kCal\n")
