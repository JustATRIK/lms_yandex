def graph(func):
    res = []
    for x in range(-10, 11):
        y = eval(func.replace('x', f'({str(x)})'))
        res.append((x, y))
    print('x\t', end='')
    for i in range(20):
        print(f'{res[i][0]}\t', end='')
    print(res[-1][0])

    print('y\t', end='')
    for i in range(20):
        print(f'{res[i][1]}\t', end='')
    print(res[-1][1])
