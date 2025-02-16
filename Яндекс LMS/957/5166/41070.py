def big_data(*data, key=lambda x: x[0]):
    data = list(map(lambda x: x + (
        x[2].split("@")[0].capitalize() + x[1].split('-')[0][0] + x[1].split('-')[1][-1] + x[1].split('-')[2][-1],),
                    data))
    return sorted(data, key=key)
    