from collections import defaultdict


def good_dreams(text, first_divisor, second_divisor, *args, **kwargs):
    funcs = defaultdict(list)
    for n, i in args:
        if n in kwargs:
            funcs[i].append(kwargs[n])

    res = []
    sp_text = text.split(first_divisor)
    for i in range(len(sp_text)):
        r = sp_text[i].split(second_divisor)
        for func in funcs[i]:
            r = list(map(func, r))
        res.append(r)
    return res
