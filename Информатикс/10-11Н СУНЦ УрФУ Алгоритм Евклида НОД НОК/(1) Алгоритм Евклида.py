def gcd(a, b, c, d):
    while b > 0:
        if a > c and (a-c)%b == 0 and b==d: return True
        a, b = b, a % b
    return False

for i in range(int(input())):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print("YES" if gcd(a, b, c, d) else "NO")