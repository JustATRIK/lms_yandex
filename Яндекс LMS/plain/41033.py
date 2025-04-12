import sys


def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


res = sum(max(map(lambda x: list(map(int, filter(is_int, x.strip().split()))), sys.stdin),
          key=lambda x: (len(x), -sum(x))))
print(-1 if res == 0 else res)
