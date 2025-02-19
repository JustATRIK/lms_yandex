import sys

t = list(map(str.strip, sys.stdin))
print(*(map(lambda x: f'{x[0]} ({x[2]});',
            sorted(list(filter(lambda x: x[1] == t[-1], list(map(lambda x: tuple(x.split(" // ")), t[:-1])))),
                   key=lambda x: x[0], reverse=True))), sep='\n')
