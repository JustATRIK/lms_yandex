from typing import Optional


def getnum_ret(a: str) -> int:
    if a in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and len(a) == 1:
        return int(a)
    else:
        return ord(a) - 55


def decimal_translator_2(a: int, b: int) -> Optional[int]:
    g: int = 0
    a_str: str = str(a)
    nums: list[str] = list(a_str)
    for i in range(len(a_str)):
        if getnum_ret(nums[i]) >= b:
            return None
        g += getnum_ret(nums[i]) * (b ** (len(a_str) - i - 1))
    return g
