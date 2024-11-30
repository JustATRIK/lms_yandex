def happy_number(rock):
    if len(str(rock)) == 2:
        return [int(str(rock)[0]), int(str(rock)[1])]
    rocks = happy_number(str(rock)[1:-1])
    rocks[0] += int(str(rock)[0])
    rocks[1] += int(str(rock)[-1])
    return rocks