def permission(a):
    code_sum = sum(map(int, list(a)))
    print("ACCESS IS ALLOWED" if sum(map(int, list(input()))) == code_sum else "ACCESS IS DENIED")
    