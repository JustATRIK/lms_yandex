a = int(input())
for i in range(2, int(a ** 0.5) + 1):
    if a % i == 0:
        print("composite")
        exit()
print("prime")