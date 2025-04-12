f = ['teen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'ten', 'eleven', 'twelve',
     'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
s = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def numerals(data):
    if data == 0:
        return 'zero'
    if data == 100:
        return 'one hundred'
    
    if data in range(10, 20):
        return f[data - 1]

    t = data // 10
    t1 = data % 10

    if t == 0:
        return s[t1 - 1]

    return f[t - 1] + (('-' + s[t1 - 1]) if t1 != 0 else '')
