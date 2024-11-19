def brackets(data):
    try:
        eval(data)
        return True
    except SyntaxError:
        return False
