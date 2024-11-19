def k0(mat):
    for i in range(1, len(mat), 2):
        mat[i], mat[i - 1] = mat[i - 1], mat[i]


def k1(mat):
    for i in range(1, len(mat[0]), 2):
        for j in range(len(mat)):
            mat[j][i], mat[j][i - 1] = mat[j][i - 1], mat[j][i]


def k2(mat):
    for i in range(len(mat)):
        for j in range(i + 1, len(mat[0])):
            mat[i][j], mat[len(mat) - i - 1][len(mat[0]) - j - 1] = mat[len(mat) - i - 1][len(mat[0]) - j - 1], mat[i][j]


def k3(mat):
    for i in range(len(mat) - 2, -1, -1):
        for j in range(i + 1, len(mat[0])):
            j = len(mat[0]) - j - 1
            mat[i][j], mat[len(mat) - i - 1][len(mat[0]) - j - 1] = mat[len(mat) - i - 1][len(mat[0]) - j - 1], mat[i][j]


def get_medicine(mat, k=0):
    match k:
        case 1:
            k0(mat)
        case 2:
            k1(mat)
        case 3:
            k2(mat)
        case 4:
            k3(mat)
