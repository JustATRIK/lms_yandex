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


def tr(a: str, b: int) -> int:
    g: int = 0
    nums: list[str] = list(a)
    for i in range(len(a)):
        g += getnum_ret(nums[i]) * (b ** (len(a) - i - 1))
    return g


def tr_ret(a: int, b: int) -> str:
    res: str = ''
    while a >= b:
        res = getnum(a % b) + res
        a //= b
    return getnum(a) + res


def gen_numbers(b: int, a: int = None) -> list[str]:
    return list(map(getnum, range(b if a is not None else 0, b if a is not None else a)))


# Z = 35 - max possib0le tr(f'3{x}15{x}', 15) + tr(f'123', tr(f'3{x}51', 10)) + getnum_ret(x)**getnum_ret(x) + tr(f'1{x}3', tr(f'1{x}3', 10)) + tr(f'1{x}2', getnum_ret(x) + 1)
A = input()
num = A
if A == '1' + ((len(A) - 1) * '0'):
    print(-(2 ** (len(A) - 1)))
    exit()
if A[0] == '1':
    num = tr_ret(tr(num, 2) - 1, 2)
    num = "".join(['1' if i == '0' else '0' for i in num])
    print(-tr(num, 2))
    exit()
print(tr(num, 2))