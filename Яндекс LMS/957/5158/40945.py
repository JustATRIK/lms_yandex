d = []


def prompter(data):
    global d
    for i in d:
        if data in i:
            return i
    d.append(data)
    return data
