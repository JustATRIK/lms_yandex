def cash_withdrawal(n):
    if n > 50000:
        return "Exceeded the limit"
    res = []
    for bill in sorted(list(atm.keys()), reverse=True):
        to_withdraw = min(n // bill, atm[bill])
        n -= to_withdraw * bill
        if to_withdraw > 0:
            res.append((bill, to_withdraw))
    if n != 0:
        return "Insufficient funds"
    else:
        return "\n".join(map(lambda x: f"{x[1]} bills of {x[0]} rubles each", res))
