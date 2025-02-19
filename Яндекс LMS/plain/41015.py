a = input().split("; ")
print(*map(lambda x: x[1:] if x[0].lower() == "*" else x, list(filter(lambda x: x[0].lower() != "v", a))), sep='\n')
