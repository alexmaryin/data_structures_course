from stack.stack import Stack


class BufferedQueue:
    def __init__(self, limit):
        self.limit = limit
        self.enqueued = Stack()
        self.dequeued = Stack()

    def __str__(self):
        return self.enqueued.__str__() + self.dequeued.__str__() + f' buffer limit {self.limit}'

    def enqueue(self, item):
        if self.size() < self.limit:
            self.enqueued.push(item)
            return True
        else:
            return False

    def dequeue(self):
        if self.dequeued.size() > 0:
            return self.dequeued.pop()
        while self.enqueued.size() > 1:
            self.dequeued.push(self.enqueued.pop())
        return self.enqueued.pop()

    def next(self):
        if self.dequeued.size() > 0:
            return self.dequeued.last()
        else:
            return self.enqueued.first()

    def last(self):
        if self.enqueued.size() > 0:
            return self.enqueued.last()
        else:
            return self.dequeued.first()

    def size(self):
        return self.enqueued.size() + self.dequeued.size()
