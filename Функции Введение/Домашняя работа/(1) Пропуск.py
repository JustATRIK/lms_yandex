code_sum = 0


def permission(a):
    global code_sum
    code_sum = sum(map(int, list(a)))


print("ACCESS IS ALLOWED" if int(input()) == code_sum else "ACCESS IS DENIED")