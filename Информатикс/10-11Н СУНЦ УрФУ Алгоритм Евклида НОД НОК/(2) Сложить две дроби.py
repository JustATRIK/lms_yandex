def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


a, b, c, d = map(int, input().split())
a1, b1 = (a * d + c * b), b * d
r = gcd(a1, b1)
print(a1 // r, b1 // r)