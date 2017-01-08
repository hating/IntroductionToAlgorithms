import random


def HashInsert(e, T, s):
    for i in range(0, s):
        if T[(e + i) % s] == -1:
            T[(e + i) % s] = e
            return True
    return False


def HashSearch(e, T, s):
    for i in range(0, s):
        if T[(e + i) % s] == e:
            return (e + i) % s
    return False


print "Now displaying Open Addressing Hash."
s = 13
A = []
T = [-1 for i in range(0, s)]
t = random.randint(5, 100)
for i in range(0, t):
    A.append(random.randint(0, 1000))
for e in A:
    HashInsert(e, T, s)
print T
e = random.choice(A)
i = HashSearch(e, T, s)
print "The selected elem ", e, " is in Slot:", i
