from typing import Generic, TypeVar, List

T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self):
        self.list: List[T] = []

    def __str__(self):
        return self.list.__str__()

    def enqueue(self, item):
        self.list.append(item)
        return True

    def dequeue(self):
        if self.list:
            return self.list.pop(0)
        else:
            return None

    def get_next(self):
        if self.list:
            return self.list[0]
        else:
            return None

    def size(self):
        return len(self.list)
