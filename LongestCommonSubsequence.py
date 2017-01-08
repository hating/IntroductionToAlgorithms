def LCSString(b, X, i, j):
    if i == -1 or j == -1:
        return
    if b[i][j] == "SLOPE":
        a = LCSString(b, X, i - 1, j - 1)
        return X[i] if a is None else a + X[i]
    elif b[i][j] == "UP":
        return LCSString(b, X, i - 1, j)
    else:
        return LCSString(b, X, i, j - 1)

def LCS(X, Y):
    b = [[0 for i in range(0, len(Y))] for i in range(0, len(X))]
    c = [[0 for i in range(0, len(Y) + 1)] for i in range(0, len(X) + 1)]
    for i in range(0, len(X)):
        for j in range(0, len(Y)):
            if X[i] == Y[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                b[i][j] = "SLOPE"
            elif c[i][j + 1] > c[i + 1][j]:
                c[i + 1][j + 1] = c[i][j + 1]
                b[i][j] = "UP"
            else:
                c[i + 1][j + 1] = c[i + 1][j]
                b[i][j] = "LEFT"
    return LCSString(b, X, len(X) - 1, len(Y) - 1)

print LCS("ABCBDAB", "BDCABA")
