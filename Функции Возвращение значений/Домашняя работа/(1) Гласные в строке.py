def vowels_in_string(data):
    data1 = []
    for i in data:
        if i in 'àÿî¸óşıåûè' or i in 'aeuioy':
            data1.append(i)
    return data1
