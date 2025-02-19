def genome(line_1, line_2):
    n = len(line_1)
    d = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    count = sum(d[line_2[i]] != line_1[i] for i in range(n))
    return n - count, 10 * count < 3 * n
