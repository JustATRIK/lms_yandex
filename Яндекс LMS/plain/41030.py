import sys


def count_divisors(n):
    if n <= 0:
        return 0
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count


print(list(sorted(list(map(lambda x: (int(x), count_divisors(int(x))), map(str.strip, list(sys.stdin)[:-1]))),
                  key=lambda x: (x[1], x[0]))))
