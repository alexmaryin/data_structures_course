from stack.stack_max_supported import StackMaxSupported


class Queue2sMaxSupported:
    def __init__(self):
        self.enqueued = StackMaxSupported()
        self.dequeued = StackMaxSupported()

    def __str__(self):
        return self.enqueued.__str__() + self.dequeued.__str__() + f' max: {self.max()}'

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

    def max(self):
        s = list(filter(lambda x: x is not None, [self.enqueued.max(), self.dequeued.max()]))
        return max(s) if len(s) > 0 else None
