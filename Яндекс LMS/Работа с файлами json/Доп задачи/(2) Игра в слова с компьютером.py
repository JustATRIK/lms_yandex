import json


with open('russian_words.json', 'r', encoding='utf-8') as f:
    dictionary = json.load(f)

players_move = True
req_l = ""
used_words = set()
while (a := input().lower()) != "сдаюсь":
    if a[0] != req_l and req_l != "":
        print(f"Это слово не на букву {req_l}.")
        continue
    elif a in used_words:
        print("Это слово уже было.")
        continue
    elif a[0] not in dictionary or a not in dictionary[a[0]]:
        print("Такого слова нет.")
        continue
    if a[-1] in {"ь", "ы"}:
        req_l = a[-2]
    else:
        req_l = a[-1]
    used_words.add(a)
    if len(set(dictionary[req_l]) - used_words) != 0:
        w = list(set(dictionary[req_l]) - used_words)[0]
        used_words.add(w)
        print(w)
        if w[-1] in {"ь", "ы"}:
            req_l = w[-2]
        else:
            req_l = w[-1]
        if len(set(dictionary[req_l]) - used_words) == 0:
            break
    else:
        print(f"Игра закончена! Победил пользователь.")
        exit()

print("Игра закончена! Победил компьютер.")
