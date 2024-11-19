months = ['€нвар€', 'феврал€', 'марта', 'апрел€', 'ма€', 'июн€', 'июл€', 'августа', 'сент€бр€', 'окт€бр€', 'но€бр€', 
          'декабр€']


def day_in_words(data):
    data = data.split('.')
    return f'{data[0]} {months[int(data[1]) - 1]} {data[2]} года'
