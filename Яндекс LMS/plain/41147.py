import random
from string import digits, ascii_lowercase, ascii_uppercase


def name(lenn):
    return ascii_lowercase[random.randint(0, len(ascii_lowercase) - 1)] + digits[random.randint(0, 9)] + " " + \
        ascii_uppercase[random.randint(0, len(ascii_uppercase) // 12 - 1)] + "".join(
            [ascii_lowercase[random.randint(0, len(ascii_lowercase) - 1)] for _ in range(lenn - 4)])
