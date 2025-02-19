def change(line, sub, symb):
    if line.count(sub) == 0:
        return line
    i = line.index(sub)
    line = line[:i] + symb + line[i + 1:]
    return change(line, sub, symb)
