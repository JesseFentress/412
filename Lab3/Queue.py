from Stack import Stack

class Queue:


    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def is_Empty(self):
        if self.s1.is_Empty() and self.s2.is_Empty():
            return True
        else:
            return False

    def size(self):
        return self.s1.size() + self.s2.size()

    def enqueue(self, item):
        self.s1.push(item)

    def dequeue(self):
        if not self.s2.is_Empty():
            return self.s2.pop()
        else:
            while self.s1.is_Empty() is False:
                self.s2.push(self.s1.pop())
            return self.s2.pop()
