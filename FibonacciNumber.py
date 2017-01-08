import random


def NaiveFibonacci(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    else:
        return NaiveFibonacci(a - 1) + NaiveFibonacci(a - 2)


def LinearFibonacci(a):
    A = [0, 1]
    for i in range(2, a + 1):
        A.append(A[i - 1] + A[i - 2])
    return A[a]


def MatrixMultiply(m1, m2):
    result = [[0 for i in range(len(m2[0]))] for i in range(len(m1))]
    for i in range(0, len(m1)):  # The number of the row is defined by m1
        for j in range(0, len(m2[0])):  # The number of column is defined by m2
            for k in range(len(m1[0])):
                result[i][j] += m1[i][k] * m2[k][j]
    return result


def RecursiveSquaring(n):
    basicMatrix = [[1, 1], [1, 0]]
    if n == 0:
        return basicMatrix  # Identity matrix
    if n == 1:
        return basicMatrix
    else:
        matrix = RecursiveSquaring(n / 2)
        if n % 2 == 0:
            return MatrixMultiply(matrix, matrix)
        if n % 2 == 1:
            return MatrixMultiply(MatrixMultiply(matrix, matrix), basicMatrix)


def AdvanceFibonacci(n):
    matrix = RecursiveSquaring(n)
    return matrix[0][1]


a = random.randint(0, 100)
print "Now Displaying Fibonacci Number(Naive Method)"
print "the Fibonacci number of ", a, " is ", NaiveFibonacci(a)
print "Now Displaying Fibonacci Number(Linear)"
print "the Fibonacci number of ", a, " is ", LinearFibonacci(a)
print "Now Displaying Fibonacci Number(logn)"
print "the Fibonacci number of ", a, " is ", AdvanceFibonacci(a)
