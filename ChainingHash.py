import random


def HashDelete(e, T, s):
    i1, i2 = HashSearch(e, T, s)
    T[i1].pop(i2)


def HashSearch(e, T, s):
    for i in range(0, len(T[e % s])):
        if T[e % s][i] == e:
            return e % s, i
    return None


def HashInsert(e, T, s):
    T[e % s].append(e)


print "Now displaying Chaining Hash"
s = 13
A = []
T = [[] for i in range(0, s)]
t = random.randint(5, 100)
for i in range(0, t):
    A.append(random.randint(0, 1000))
for e in A:
    HashInsert(e, T, s)
print T
e = random.choice(A)

i1, i2 = HashSearch(e, T, s)
print "The selected elem ", e, " is in Slot:", i1, " Position: ", i2
HashDelete(e, T, s)
print "After Deletion:"
print T