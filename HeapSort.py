import random


def MaxHeapify(A, i, s):
    l = i * 2
    r = i * 2 + 1
    largest = i
    if l < s and A[l] > A[i]:
        largest = l
    if r < s and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MaxHeapify(A, largest, s)


def BuildMaxHeap(A, s):
    for i in range(0, len(A) / 2)[::-1]:
        MaxHeapify(A, i, s)
    return A


def HeapSort(A):
    s = len(A)
    BuildMaxHeap(A, s)

    for i in range(1, len(A))[::-1]:
        A[0], A[i] = A[i], A[0]
        s -= 1
        MaxHeapify(A, 0, s)
    return A


print "Now displaying HeapSort"
A = []
s = random.randint(5, 100)
for i in range(0, s):
    A.append(random.randint(0, 1000))
print A
print HeapSort(A)
