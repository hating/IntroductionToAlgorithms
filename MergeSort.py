import random


def MergeSort(A, p, r):
    q = (p + r) / 2  # Find the middle
    if p < r:
        MergeSort(A, p, q)  # MergeSort A[p...q]
        MergeSort(A, q + 1, r)  # MergeSort A[p+1....r]
    return Merge(A, p, q, r)


# The guard in Merge()
MAX = 10000


def Merge(A, p, q, r):
    L = []
    R = []
    for i in range(p, q + 1):  # Copy the left side.
        L.append(A[i])
    for i in range(q + 1, r + 1):  # Copy the right side.
        R.append(A[i])
    L.append(MAX)  # Add guard to the end.
    R.append(MAX)  # Add guard to the end.
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] < R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    return A


print "Now displaying MergeSort"
A = []
s = random.randint(5, 100)
for i in range(0, s):
    A.append(random.randint(0, 1000))
print A
print MergeSort(A, 0, len(A) - 1)
