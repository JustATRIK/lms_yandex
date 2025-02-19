def tunnel(rock):
    if len(rock) == 1:
        return rock[0]
    elif len(rock) == 2:
        return rock[0] + rock[1]
    return tunnel(rock[1:-1])
