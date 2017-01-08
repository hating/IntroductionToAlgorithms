import random


class Stack:
    def __init__(self):
        self.top = -1
        self.s = 100
        self.S = [0 for i in range(0, self.s)]

    def StackEmpty(self):
        if self.top == -1:
            return True
        return False

    def Push(self, x):
        if self.top == self.s - 1:
            return False
        self.top += 1
        self.S[self.top] = x
        return True

    def Pop(self):
        if self.StackEmpty():
            return False
        else:
            self.top -= 1
            return self.S[self.top + 1]


S = Stack()
for i in range(0, 120):
    S.Push(random.randint(0,999))

while not S.StackEmpty():
    print S.Pop()
