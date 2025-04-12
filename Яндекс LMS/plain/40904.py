def brackets(data):
    a = 0
    for i in data:
        if i == '(':
            a += 1
        elif i == ')':
            a -= 1
        if a <= -1:
            return False
    if abs(a) != 0:
        return False
    return True
