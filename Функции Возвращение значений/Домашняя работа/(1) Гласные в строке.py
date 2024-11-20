def vowels_in_string(data):
    data1 = []
    for i in data:
        if i in 'аяоёуюэеыи' or i in 'aeuioy':
            data1.append(i)
    return data1
