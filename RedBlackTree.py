class Node:
    def __init__(self, key, left=None, right=None, color=None, p=None):
        self.left = left
        self.right = right
        self.color = color
        self.key = key
        self.p = p
        if key == "NIL":
            self.p = self

    def LeftRotate(self, T, x):
        y = x.right
        x.right = y.left
        if y.left != T.nil:
            y.left.p = x
        y.p = x.p
        if x.p == T.nil:
            T.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def RightRotate(self, T, x):
        y = x.left
        x.left = y.right
        if y.right != T.nil:
            y.right.p = x
        y.p = x.p
        if x.p == T.nil:
            T.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.right = x
        x.p = y

    def RBInsert(self, T, z):
        y = T.nil
        x = T.root
        while x != T.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == T.nil:
            T.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = T.nil
        z.right = T.nil
        z.color = "RED"
        self.RBInsertFixUp(T, z)

    def TreeHeight(self, T, z):
        if z == T.nil:
            return 0
        lh = self.TreeHeight(T, z.left)
        rh = self.TreeHeight(T, z.right)
        if lh > rh:
            return lh + 1
        return rh + 1

    def RBInsertFixUp(self, T, z):
        while z.p.color == "RED":
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == "RED":
                    z.p.color = "BLACK"
                    y.color = "BLACK"
                    z.p.p.color = "RED"
                    z = z.p.p
                elif z == z.p.right:
                    z = z.p
                    self.LeftRotate(T, z)
                z.p.color = "BLACK"
                if z.p.p != T.nil:
                    z.p.p.color = "RED"
                    self.RightRotate(T, z.p.p)
            else:
                y = z.p.p.left
                if y.color == "RED":
                    z.p.color = "BLACK"
                    y.color = "BLACK"
                    z.p.p.color = "RED"
                    z = z.p.p
                elif z == z.p.left:
                    z = z.p
                    self.RightRotate(T, z)
                z.p.color = "BLACK"
                if z.p.p != T.nil:
                    z.p.p.color = "RED"
                    self.LeftRotate(T, z.p.p)
        T.root.color = "BLACK"

    def RBTransplant(self, T, u, v):
        if u.p == T.nil:
            T.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def TreeMinimum(self, T, z):
        if z.left != T.nil:
            return self.TreeMinimum(T, z.left)
        else:
            return z

    def RBDeleteFixUp(self, T, x):
        while x != T.root and x.color == "BLACK":
            if x == x.p.left:
                w = x.p.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.p.color = "RED"
                    self.LeftRotate(T, x.p)
                    w = x.p.right
                if w !=T.nil :
                    if w.left.color == "BLACK" and w.right.color == "BLACK":
                        w.color = "RED"
                        x = x.p
                    elif w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self.RightRotate(T, w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = "BLACK"
                    w.right.color = "BLACK"
                    self.LeftRotate(T, x.p)
                x = T.root
            else:
                w = x.p.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.p.color = "RED"
                    self.RightRotate(T, x.p)
                    w = x.p.left
                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.p
                elif w.left.color == "BLACK":
                    w.right.color = "BLACK"
                    w.color = "RED"
                    self.LeftRotate(T, w)
                    w = x.p.left
                w.color = x.p.color
                x.p.color = "BLACK"
                w.left.color = "BLACK"
                self.RightRotate(T, x.p)
                x = T.root
        x.color = "BLACK"

    def RBDelete(self, T, z):
        y = z
        yOriginalColor = y.color
        if z.left == T.nil:
            x = z.right
            self.RBTransplant(T, z, z.right)
        elif z.right == T.nil:
            x = z.left
            self.RBTransplant(T, z, z.left)
        else:
            y = self.TreeMinimum(T, z.right)
            yOriginalColor = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.RBTransplant(T, y, y.right)
                y.right = z.right
                y.right.p = y
            self.RBTransplant(T, z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if yOriginalColor == "BLACK":
            self.RBDeleteFixUp(T, x)

    def InOrderTraversal(self, T, s, A):
        if s == T.nil :
            return
        if s.left != T.nil:
            self.InOrderTraversal(T, s.left, A)
        A.append(s)
        if s.right != T.nil:
            self.InOrderTraversal(T, s.right, A)


class Tree:
    def __init__(self):
        nil = Node("NIL", color="BLACK")
        self.root = nil
        self.nil = nil


T = Tree()
B = [11, 2, 14, 1, 7, 15, 5, 8, 4]
BB = [26]
for j in B:
    T.root.RBInsert(T, Node(j))
    print j
A = []
T.root.InOrderTraversal(T, T.root, A)
for i in A:
    T.root.RBDelete(T, i)
    AA = []
    T.root.InOrderTraversal(T, T.root, AA)
    print "AfterDeleting ", i.key, ".Nodes in tree:", [AAA.key for AAA in AA]
