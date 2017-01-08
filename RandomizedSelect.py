import random


def RandomizedPartition(A, p, r):
    it = random.randint(p, r)
    A[p], A[it] = A[it], A[p]
    x = A[p]  # To get a randomized elem.
    i = p - 1
    for j in range(p, r + 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[p], A[i] = A[i], A[p]
    return i


def RandomizedSelect(A, p, r, i):
    # if p == r:
    #     return A[p]
    q = RandomizedPartition(A, p, r)
    if q == i:
        return A[q]
    if q > i:
        return RandomizedSelect(A, p, q - 1, i)
    if q < i:
        return RandomizedSelect(A, q + 1, r, i)


print "Now displaying Randomized Select"
A = []
s = random.randint(5, 100000)
for i in range(0, s):
    A.append(random.randint(0, 100000000))
# print A
i = random.randint(0, s - 1)
print "The position of ", i, "is :", RandomizedSelect(A, 0, len(A) - 1, i)
A.sort()
print A[i]
