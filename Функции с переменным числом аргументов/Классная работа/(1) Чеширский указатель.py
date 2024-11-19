s = input().split()
a = []
for i in s[1:-1]:
    if s[0].lower() <= i.lower() <= s[-1].lower():
        a.append(i)
print(*a)
