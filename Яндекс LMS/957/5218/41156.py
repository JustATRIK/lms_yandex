import math


def multiplier(*nums, key=None):
    nums = list(filter(lambda x: key(x), nums))
    return math.prod(nums) if len(nums) > 0 else None
