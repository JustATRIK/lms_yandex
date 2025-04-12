def vowels_in_string(data):
    data1 = []
    for i in data:
        if i.lower() in 'аяоёуюэеыи' or i.lower() in 'aeuioy':
            data1.append(i)
    return data1
