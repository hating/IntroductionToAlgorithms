import random


def Partition(A, p, r):
    x = A[p]  # To get a randomized elem.
    i = p - 1
    for j in range(p, r + 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[p], A[i] = A[i], A[p]
    return i


def QuickSort(A, p, r):
    if r > p:
        q = Partition(A, p, r)
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)
    return A


def MiddlePartition(A, p, r):
    # To get the middle of the elem.
    T = [[A[i] for i in range(j * 5, j * 5 + 5)] for j in range(0, (0 + len(A)) / 5)]
    m = []
    for i in T:
        QuickSort(i, 0, 4)
        m.append(i[2])
    QuickSort(m, 0, len(m) - 1)
    mm = m[len(m) / 2]

    x = mm
    i = p - 1
    for j in range(p, r + 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[p], A[i] = A[i], A[p]
    return i


def MiddleSelect(A, p, r, i):
    if p == r:
        return A[p]
    q = MiddlePartition(A, p, r)
    if q == i:
        return A[q]
    if q > i:
        return MiddleSelect(A, p, q - 1, i)
    if q < i:
        return MiddleSelect(A, q + 1, r, i)


print "Now displaying Middle Select"
A = []
s = random.randint(5, 100)
for i in range(0, s):
    A.append(random.randint(0, 1000))
print A
i = random.randint(0, s)
print "The position of ", i, "is :", MiddleSelect(A, 0, len(A) - 1, i)

