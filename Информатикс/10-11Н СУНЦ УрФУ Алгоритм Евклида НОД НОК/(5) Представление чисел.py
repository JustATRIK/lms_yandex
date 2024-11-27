def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def is_prime(a):
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


a = int(input())
if is_prime(a):
    print(1, a - 1)
    exit()

for i in range(2, int(a ** 0.5) + 1):
    if a % i == 0 and gcd(a, a / i) == gcd(a, a - a / i):
        print(a // i, a - a // i)
        exit()