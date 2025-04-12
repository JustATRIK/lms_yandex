n = 0


def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


def next_prime_number():
    global n
    n += 1
    while not is_prime(n):
        n += 1
    print(n)
