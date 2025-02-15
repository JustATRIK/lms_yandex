from math import log2


s = input()
print(len(s) * log2(len(set(s))))
