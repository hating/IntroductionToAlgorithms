import random


def Partition(A, p, r):
    it = random.randint(p, r)  # To get a randomized elem.
    A[p], A[it] = A[it], A[p]
    x = A[p]
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


print "Now displaying QuickSort"
A = []
s = random.randint(5, 100)
for i in range(0, s):
    A.append(random.randint(0, 1000))
print A
print QuickSort(A, 0, len(A) - 1)
