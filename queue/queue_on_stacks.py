from stack.stack import Stack
from typing import Generic, TypeVar

T = TypeVar('T')


class Queue2s(Generic[T]):
    def __init__(self):
        self.enqueued = Stack[T]()
        self.dequeued = Stack[T]()

    def __str__(self):
        return self.enqueued.__str__() + self.dequeued.__str__()

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
