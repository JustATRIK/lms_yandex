a = input().split()
print(", ".join(filter(lambda x: len(set(x.lower()) & set(a[1].lower())) >= 6, a)))
