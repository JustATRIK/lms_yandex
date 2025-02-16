data = []


def refinement(new_data):
    data.extend(new_data)
    mod = sum(data) % 2
    fil = list(filter(lambda x: x % 2 == mod, data))
    if len(fil) == 0:
        return 0
    return sum(fil) / len(fil)
