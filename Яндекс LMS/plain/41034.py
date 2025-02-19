import sys

print(*map(lambda x: f'{x[0]}: {x[2]}; {x[1]}', sorted(map(lambda x: tuple(x.strip().split(", ")), list(sys.stdin)[1:]),
                                                       key=lambda x: (-int(x[1]), x[0], float(x[2])))), sep='\n')
