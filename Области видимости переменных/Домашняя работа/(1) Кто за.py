za = 0
protiv = 0


def voting(d):
    global za, protiv
    if d == "��":
        za += 1
    else:
        protiv += 1
    print(f"��: {za}\n������: {protiv}\n")