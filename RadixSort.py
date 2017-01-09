import random


def GetI(n):
    i = 0
    while n != 0:
        n /= 10
        i += 1
    return i


def GetKey(n, i):
    ret = n
    ret /= pow(10, i)
    return ret % 10


def RadixSort(A):
    for i in range(0, GetI(A[0])):
        A.sort(lambda x, y: cmp(GetKey(x, i), GetKey(y, i)))
    return A


print "Now displaying Radix Sort."
A = []
s = random.randint(4, 100)
for i in range(0, s):
    A.append(random.randint(0, 999))
print A
print RadixSort(A)
print "DEBUG"
