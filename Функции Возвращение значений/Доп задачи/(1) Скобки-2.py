def brackets(data):
    a = '{[(<'
    b = '}])>'
    c = 'o'
    for i in data:
        if i in a:
            c += b[a.index(i)]
        elif i in b:
            if i != c[-1]:
                return False
            c = c[:len(c) - 1]
    return True
