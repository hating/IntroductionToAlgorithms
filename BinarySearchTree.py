import random


class Tree:
    def __init__(self):
        self.l = None
        self.r = None
        self.k = None
        self.p = None

    def Transplant(self, u, v):
        if u.p is None:
            u.k = v.k

        elif u is u.p.l:
            u.p.l = v
        else:
            u.p.r = v
        if v.k is not None:
            v.p = u.p

    def TreeDelete(self, z):

        if z.l.k is None:
            self.Transplant(z, z.r)
        elif z.r.k is None:
            self.Transplant(z, z.l)
        else:
            y = z.r.TreeMinimum()
            if y.p is not z:
                self.Transplant(y, y.r)
                y.r = z.r
                y.r.p = y
            self.Transplant(z, y)
            y.l = z.l
            y.l.p = y

    def Insert(self, T, i, P):
        if T.k == None:
            T.k = i
            T.p = P
            T.l = Tree()
            T.r = Tree()
        elif T.k > i:
            self.Insert(T.l, i, T)
        elif T.k < i:
            self.Insert(T.r, i, T)

    def Sort(self, A):
        # random.shuffle(A) # This is use to get randomized Tree.
        for i in range(0, len(A)):
            self.Insert(self, A[i], None)

    def InOrderTreeWalk(self, A):
        if self.k is not None:
            self.l.InOrderTreeWalk(A)
            A.append(self)
            self.r.InOrderTreeWalk(A)

    def TreeSearch(self, k):
        if self.k == k or self.k is None:
            return self
        elif k < self.k:
            return self.l.TreeSearch(k)
        else:
            return self.r.TreeSearch(k)

    def IterativeTreeSearch(self, k):
        while self.k is not None and self.k != k:
            if k < self.k:
                self = self.l
            else:
                self = self.r
        return self

    def TreeMinimum(self):
        while self.l.k is not None:
            self = self.l
        return self

    def TreeMaxinum(self):
        while self.r.k is not None:
            self = self.r
        return self


A = []
s = random.randint(5, 100)
for i in range(0, s):
    A.append(random.randint(0, 1000))
k = random.choice(A)
t = Tree()
t.Sort(A)
A = []
t.InOrderTreeWalk(A)
print "Using InOrderWalk:", [A[i].k for i in range(0, len(A))]
print "Using Recursion method to find ", k, " :", t.TreeSearch(k).k
print "Using Interval method to find ", k, " :", t.IterativeTreeSearch(k).k
print "Finding the Minimum elem :", t.TreeMinimum().k
print "Finding the Maximum elem :", t.TreeMaxinum().k
d = random.choice([A[i].k for i in range(len(A))])
print "we are going to delete:",d
t.TreeDelete(t.TreeSearch(d))
B = []
t.InOrderTreeWalk(B)
print "After deletion:",[B[i].k for i in range(0, len(B))]
