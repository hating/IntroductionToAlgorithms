class Node:
    def __init__(self, key, prev=None, next_=None):
        self.key = key
        self.prev = prev
        self.next_ = next_


class List:
    def __init__(self):
        self.nil = Node("NIL")
        self.nil.next_ = self.nil
        self.nil.prev = self.nil
        # Two guards link together.

    def ListInsert(self, x):
        x.next_ = self.nil.next_
        self.nil.next_.prev = x
        self.nil.next_ = x
        x.prev = self.nil

    def ListSearch(self, k):
        x = self.nil.next_
        while x.key != k and x != self.nil:
            x = x.next_
        return x

    def ListDelete(self, x):
        x.prev.next_ = x.next_
        x.next_.prev = x.prev


L = List()
for i in range(0, 5):
    L.ListInsert(Node(i))
A = []
for i in range(0, 5):
    A.append(L.ListSearch(i))
    print A[i].key
for i in A:
    L.ListDelete(i)
print "DEBUG"
