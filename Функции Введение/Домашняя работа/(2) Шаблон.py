def template(a, b, c):
    if not (a + b > c and b + c > a and c + a > b):
        print(None)
        return

    p = (a + b + c) / 2
    print(f"""Периметр: {a + b + c}
Площадь: {(p * (p - a) * (p - b) * (p - c)) ** 0.5}
Равнобедренный: {"да" if a == b or b == c or c == a else "нет"}
Равносторонний: {"да" if a == b == c else "нет"}""")
