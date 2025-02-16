a, n = int(input()), int(input())
b = [list(map(int, input().split())) for i in range(n)]
print(sum(map(lambda y: sum(filter(lambda x: x >= a, y)), b)))