a = input().split()
max_len = len(max(a, key=len))
a = list(map(lambda x: (max_len - len(x)) * '*' + x, a))
print(*a, sep='\n')