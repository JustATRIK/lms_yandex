divisors = {}


def number_of_divisors(n):
    if n in divisors:
        return divisors[n]
    divisors[n] = 0
    for i in range(1, int(n ** 0.5 + 1)):
        if n % i == 0:
            divisors[n] += 2 if i ** 2 != n else 1
    return divisors[n]
