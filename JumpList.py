import random


class Node:
    def __init__(self, key, next_=None, prev=None, down=None):
        self.key = key
        self.next_ = next_
        self.prev = prev
        self.down = down


class List:
    def __init__(self):
        minNum, maxNum = -1, 10000
        self.L = Node(minNum)
        E = Node(maxNum)
        self.L.next_, E.prev = E, self.L


class JList:
    def __init__(self):
        self.JL = []
        self.JL.append(List())

    def AddLevel(self):
        self.JL.append(List())
        self.JL[len(self.JL) - 1].L.down = self.JL[len(self.JL) - 2].L

    def Add(self, key):
        e = Node(key)
        i = 0
        while random.randint(0, 9) % 2 == 0:
            i += 1
        while len(self.JL) < i + 1:
            self.AddLevel()
        it = self.JL[i].L
        while it.key < e.key:
            it = it.next_
        e.next_ = it
        e.prev = it.prev
        it.prev.next_ = e
        it.prev = e
        self.RecursiveAdd(e.prev.down, e, key)
        return True

    def RecursiveAdd(self, itt, e, key):
        if itt == None:
            return
        e.down = en = Node(key)
        while itt.key < en.key:
            itt = itt.next_
        en.next_ = itt
        en.prev = itt.prev
        itt.prev.next_ = en
        itt.prev = en
        itt = en.prev.down
        self.RecursiveAdd(itt, en, key)

    def Search(self, key, Level=None):
        i = self.JL[len(self.JL) - 1].L if Level is None else Level
        while i.key < key:
            i = i.next_
        if i.prev.down != None:
            return self.Search(key, i.prev.down)
        elif i.key == key:
            return i
        else:
            return False

    def Delete(self, key, Level=None):
        i = self.JL[len(self.JL) - 1].L if Level is None else Level
        while i.key < key:
            i = i.next_
        if i.key == key:
            i.prev.next_ = i.next_
            i.next_.prev = i.prev
            while i.down is not None:
                i = i.down
                i.prev.next_ = i.next_
                i.next_.prev = i.prev
        elif i.prev.down != None:
            return self.Delete(key, i.prev.down)
        else:
            return False

test = JList()
for i in range(0, 10):
    test.Add(i)
n = test.Search(6)
for i in range(0, 1024):
    test.Delete(i)
