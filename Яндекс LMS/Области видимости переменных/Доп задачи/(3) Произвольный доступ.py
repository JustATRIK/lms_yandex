def write_file(file, memory, capacity=1):
    free_spaces = 0
    for i in memory:
        free_spaces += i.count(0)
    if len(file) > free_spaces * capacity:
        return
    for i in range(len(memory)):
        for j in range(len(memory[0])):
            if memory[i][j] == 0:
                memory[i][j] = 1
                coords = (None, None, None)
                if file[capacity:] != "":
                    coords = write_file(file[capacity:], memory, capacity)
                a = (file[:capacity], coords[1], coords[2])
                memory[i][j] = a
                return file[:capacity], i, j


def read_file(memory, coords):
    res = ""
    while coords != (None, None):
        a = memory[coords[0]][coords[1]]
        res += a[0]
        coords = (a[1], a[2])
    return res
