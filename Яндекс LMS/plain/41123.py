import csv
import json


def check_security(name, place):
    region_key = -1
    with open("regions.csv", encoding="utf-8") as f:
        data = list(csv.reader(f, delimiter=";"))[1:]
        for key, region_name in data:
            if region_name == place:
                region_key = key
                break
    with open("taxpayer_in.json", "r", encoding="utf-8") as f:
        payers = json.loads(f.read())
        tin = None
        for payer in payers:
            if (payer["lastname"], payer["firstname"], payer["middlename"]) == name:
                tin = payer["tin"]
                break
        if not tin:
            return None, None
    res = [-1, -1]
    if region_key == tin[:2]:
        res[0] = 0
    checksum = 0
    for digit, p in zip(tin[:10], (7, 2, 4, 10, 3, 5, 9, 4, 6, 8)):
        checksum += int(digit) * p
    if str(checksum % 11)[-1] != tin[10]:
        return res
    checksum = 0
    for digit, p in zip(tin[:11], (3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8)):
        checksum += int(digit) * p
    if str(checksum % 11)[-1] == tin[11]:
        res[1] = 0
    return res
