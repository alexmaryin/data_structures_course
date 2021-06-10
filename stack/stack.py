from typing import Generic, TypeVar, List

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self):
        self.list: List[T] = []

    def __str__(self):
        return self.list.__str__()

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if self.list:
            return self.list.pop()
        else:
            return None

    def last(self):
        if self.list:
            return self.list[self.size() - 1]
        else:
            return None

    def first(self):
        if self.list:
            return self.list[0]
        else:
            return None

    def size(self):
        return len(self.list)
