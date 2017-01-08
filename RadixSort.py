import random


def RadixSort(A):
    pass
    # Todo Fix it later.

def CountingSort(A, k):
    B = [0 for i in range(0, len(A))]  # The return Copy of A
    C = [0 for i in range(0, k + 1)]
    for j in range(0, len(A)):
        C[A[j]] += 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    for j in range(0, len(A))[::-1]:
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1
    return B


print "Now displaying Radix Sort."
A = []
s = random.randint(4, 100)
for i in range(0, s):
    A.append(random.randint(100, 999))
print A
print RadixSort(A, 100)
