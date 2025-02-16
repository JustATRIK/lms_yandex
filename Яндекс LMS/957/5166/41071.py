def creators(name, planets=8, alive=True):
    return f"""Система звезды {name}.
Количество планет: {planets}.
{"Жизнь есть!" if alive else "Жизни нет."}"""
