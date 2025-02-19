def sortt(str):
    c = 0
    for i in range(len(str)):
        if i % 2 == 1 and str[i].upper() in "AEIOUY":
            c += 1
    return c


def secret_sort():
    secret_avatars.sort(key=sortt)
    