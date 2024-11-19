divisors = {}


def number_of_divisors(n):
    if n in divisors:
        return divisors[n]
    count = 1 if n == 1 else 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0 and i != n:
            count += 2
    divisors[n] = count
    return count
