months = ['������', '�������', '�����', '������', '���', '����', '����', '�������', '��������', '�������', '������', 
          '�������']


def day_in_words(data):
    data = data.split('.')
    return f'{data[0]} {months[int(data[1]) - 1]} {data[2]} ����'
