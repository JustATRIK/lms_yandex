import json
import random

with open('words.json', 'r') as f:
    words_data = json.loads(f.read())

while True:
    try:
        length = int(input().strip())
        str_length = str(length)
        if str_length not in words_data or not (5 <= length <= 12):
            print("Invalid length. Please enter a length between 5 and 12.")
            continue
        break
    except ValueError:
        print("Bad input. Please enter a number.")

word = random.choice(words_data[str_length]).lower()
max_penalty = len(word)
check = 0
guessed = set()
wrong = set()

print(f"Your word {'*' * len(word)}. Enter the letter.")

while True:
    while True:
        letter = input().strip().lower()
        if len(letter) == 1 and letter.isalpha():
            break
        print("Bad input. Try once more, please.")

    if letter in word:
        guessed.add(letter)
        current_display = ''.join([c if c in guessed else '*' for c in word])
        if '*' not in current_display:
            print(f"You win! Your word is {word.upper()}.")
            exit()
        print(f"Your word {current_display}. Enter the letter.")
    else:
        wrong.add(letter)
        check += 1
        if check >= max_penalty:
            print(f"You loss! Word was {word.upper()}.")
            exit()
        current_display = ''.join([c if c in guessed else '*' for c in word])
        print(f"There is no such letter in the word. Check is {check}.")
        print(f"Your word {current_display}. Enter the letter.")
