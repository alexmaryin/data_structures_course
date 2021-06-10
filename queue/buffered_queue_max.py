from stack.stack_max_supported import StackMaxSupported


class BufferedQueueMaxSupported:
    def __init__(self, limit):
        self.buffer = limit
        self.enqueued = StackMaxSupported()
        self.dequeued = StackMaxSupported()

    def __str__(self):
        return self.enqueued.__str__() + self.dequeued.__str__() + f' max: {self.max()} buffer: {self.buffer}'

    def enqueue(self, item):
        if self.size() < self.buffer:
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

    def size(self):
        return self.enqueued.size() + self.dequeued.size()

    def max(self):
        s = list(filter(lambda x: x is not None, [self.enqueued.max(), self.dequeued.max()]))
        return max(s) if len(s) > 0 else None

    def next(self):
        if self.dequeued.size() > 0:
            return self.dequeued.last()
        else:
            return self.enqueued.first()
