from stack.stack_min_supported import StackMinSupported


class Queue2sMinSupported:
    def __init__(self):
        self.enqueued = StackMinSupported()
        self.dequeued = StackMinSupported()

    def __str__(self):
        return self.enqueued.__str__() + self.dequeued.__str__() + f' min: {self.min()}'

    def enqueue(self, item):
        self.enqueued.push(item)

    def dequeue(self):
        if self.dequeued.size() > 0:
            return self.dequeued.pop()
        while self.enqueued.size() > 1:
            self.dequeued.push(self.enqueued.pop())
        return self.enqueued.pop()

    def size(self):
        return self.enqueued.size() + self.dequeued.size()

    def min(self):
        return min(self.enqueued.min(), self.dequeued.min())
