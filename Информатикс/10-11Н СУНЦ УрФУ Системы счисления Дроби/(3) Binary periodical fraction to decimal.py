def getnum(a: int) -> str:
    if 10 > a > -1:
        return str(a)
    else:
        return chr(55 + a)


def getnum_ret(a: str) -> int:
    if a in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and len(a) == 1:
        return int(a)
    else:
        return ord(a) - 55


def tr_periodic(a: str, b: int) -> float:
    periodic = a[a.index('('):a.index(')') + 1]
    return tr(a.replace(periodic, a[a.index('(') + 1:a.index(')')] * 32), b)


def tr(a: str, b: int) -> float:
    g: float = 0
    nums: list[str] = list(a)
    t = -1
    if '.' in a:
        t = a.index('.')
    for i in range(len(a)):
        if a[i] == '.':
            continue
        g += getnum_ret(nums[i]) * (
                    b ** (len(a) - i - 1 - (len(a) - t - 1 if t <= i and t != -1 else len(a) - t if t != -1 else 0)))
    return g


def tr_ret_periodic(a: str, b: int, c=33, force_zero=False) -> str:
    periodic = a[a.index('('):a.index(')') + 1]
    return tr_ret(float(a.replace(periodic, a[a.index('(') + 1:a.index(')')] * 4)), b, c=c, force_zero=force_zero)


def tr_ret(a: float, b: int, c=33, force_zero=False) -> str:
    res: str = ''
    p = a
    while p >= b:
        res = getnum(int(p) % b) + res
        p //= b
    res = getnum(int(p)) + res
    if a - int(a) != 0:
        res += '.'
        for i in range(c):
            a = a - int(a)
            a *= b
            res += str(int(a))
    elif force_zero:
        res += '.' + '0' * c
    return res


def gen_numbers(b: int, a: int = None) -> list[str]:
    return list(map(getnum, range(b if a is not None else 0, b if a is not None else a)))


# Z = 35 - max possib0le tr(f'3{x}15{x}', 15) + tr(f'123', tr(f'3{x}51', 10)) + getnum_ret(x)**getnum_ret(x) + tr(f'1{x}3', tr(f'1{x}3', 10)) + tr(f'1{x}2', getnum_ret(x) + 1)
a = input()
if '(' in a:
    print(tr_periodic(a, 2))
else:
    print(tr(a, 2))