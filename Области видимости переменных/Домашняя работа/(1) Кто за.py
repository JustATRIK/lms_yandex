za = 0
protiv = 0


def voting(d):
    global za, protiv
    if d == "за":
        za += 1
    else:
        protiv += 1
    print(f"за: {za}\nпротив: {protiv}\n")