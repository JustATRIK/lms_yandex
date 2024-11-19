data = []


def refinement(new_data):
    data.extend(new_data)
    mod = sum(data) % 2
    fil = list(filter(lambda x: x % 2 == mod, data))
    return sum(fil) / len(fil)
