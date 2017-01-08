class Queue_():
    def __init__(self, length=10):
        self.head = 0
        self.tail = 1
        self.length = length
        self.Q = [0 for i in range(self.length)]
        # Actually there are only length-1 spaces in Q.
        # And we need to leave one space to determine whether fullStack or emptyStack.
        # So the available space is length - 2

    def QueueEmpty(self):
        if (self.head + 1) % self.length == self.tail:
            return True
        return False

    def QueueFull(self):
        if (self.tail + 1) % self.length == self.head:
            return True
        return False

    def Enqueue(self, x):
        if self.QueueFull():
            return False
        else:
            self.Q[self.tail] = x
            self.tail = (self.tail + 1) % self.length
            return True

    def Dequeue(self):
        if self.QueueEmpty():
            return None
        else:
            self.head += 1
            return self.Q[self.head]


Q = Queue_()
for i in range(0, 10):
    Q.Enqueue(i)

while not Q.QueueEmpty():
    print Q.Dequeue()
