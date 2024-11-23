a = "аяоёуюэеиы"


def vowels_in_words(words):
    d = {}
    for word in words:
        for letter in word:
            if letter in a:
                if letter in d and word in d[letter]:
                    continue

                if letter in d:
                    d[letter].append(word)
                else:
                    d[letter] = [word]
    return d
