months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 
          'декабря']


def day_in_words(data):
    data = data.split('.')
    return f'{data[0]} {months[int(data[1]) - 1]} {data[2]} года'
