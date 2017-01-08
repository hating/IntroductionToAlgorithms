import random


def MatrixPlus(m1, m2):
    return [[m1[i][j] + m2[i][j] for j in range(len(m1))] for i in range(len(m2))]


def MatrixMultiply(m1, m2):
    result = [[0 for i in range(len(m2[0]))] for i in range(len(m1))]
    for i in range(0, len(m1)):  # The number of the row is defined by m1
        for j in range(0, len(m2[0])):  # The number of column is defined by m2
            for k in range(len(m1[0])):
                result[i][j] += m1[i][k] * m2[k][j]
    return result


def Merge(C00, C01, C10, C11):
    l = len(C00) * 2
    ret = [[0 for i in range(l)] for i in range(l)]
    for i in range(l / 2):
        for j in range(l / 2):
            ret[i][j] = C00[i][j]
            ret[i][j + l / 2] = C01[i][j]
            ret[i + l / 2][j] = C10[i][j]
            ret[i + l / 2][j + l / 2] = C11[i][j]
    return ret


def MatrixMinus(m1, m2):
    return [[m1[i][j] - m2[i][j] for j in range(len(m1))] for i in range(len(m2))]


def Split(M):
    q = len(M) / 2
    MM00 = [[M[i][j] for j in range(0, q)] for i in range(0, q)]
    MM01 = [[M[i][j] for j in range(q, len(M))] for i in range(0, q)]
    MM10 = [[M[i][j] for j in range(0, q)] for i in range(q, len(M))]
    MM11 = [[M[i][j] for j in range(q, len(M))] for i in range(q, len(M))]
    return MM00, MM01, MM10, MM11


def StrassenAlgorithm(A, B):
    if len(A) == 2:
        M1 = (A[0][0] + A[1][1]) * (B[0][0] + B[1][1])
        M2 = (A[1][0] + A[1][1]) * B[0][0]
        M3 = A[0][0] * (B[0][1] - B[1][1])
        M4 = A[1][1] * (B[1][0] - B[0][0])
        M5 = (A[0][0] + A[0][1]) * B[1][1]
        M6 = (A[1][0] - A[0][0]) * (B[0][0] + B[0][1])
        M7 = (A[0][1] - A[1][1]) * (B[1][0] + B[1][1])
        C00 = M1 + M4 - M5 + M7
        C01 = M3 + M5
        C10 = M2 + M4
        C11 = M1 - M2 + M3 + M6
        return [[C00, C01], [C10, C11]]
    else:
        pass
        AA00, AA01, AA10, AA11 = Split(A)
        BB00, BB01, BB10, BB11 = Split(B)
        M1 = StrassenAlgorithm(MatrixPlus(AA00, AA11), MatrixPlus(BB00, BB11))
        M2 = StrassenAlgorithm(MatrixPlus(AA10, AA11), BB00)
        M3 = StrassenAlgorithm(AA00, MatrixMinus(BB01, BB11))
        M4 = StrassenAlgorithm(AA11, MatrixMinus(BB10, BB00))
        M5 = StrassenAlgorithm(MatrixPlus(AA00, AA01), BB11)
        M6 = StrassenAlgorithm(MatrixMinus(AA10, AA00), MatrixPlus(BB00, BB01))
        M7 = StrassenAlgorithm(MatrixMinus(AA01, AA11), MatrixPlus(BB10, BB11))
        CC00 = MatrixPlus(MatrixMinus(MatrixPlus(M1, M4), M5), M7)
        CC01 = MatrixPlus(M3, M5)
        CC10 = MatrixPlus(M2, M4)
        CC11 = MatrixPlus(MatrixPlus(MatrixMinus(M1, M2), M3), M6)
        return Merge(CC00, CC01, CC10, CC11)


s = pow(2, random.randint(1, 6))
m1 = [[random.randint(2, 100) for i in range(s)] for i in range(s)]
m2 = [[random.randint(2, 100) for i in range(s)] for i in range(s)]
print "Now displaying StrassenAlgorithm."
m = StrassenAlgorithm(m1, m2)
print StrassenAlgorithm(m1, m2)
print MatrixMultiply(m1, m2)
