from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self):
        self.list: List[T] = []

    def __str__(self):
        return self.list.__str__()

    @property
    def is_empty(self):
        return not self.list

    def push(self, item: T):
        self.list.append(item)

    def pop(self) -> Optional[T]:
        if self.list:
            return self.list.pop()
        else:
            return None

    def last(self) -> Optional[T]:
        if self.list:
            return self.list[self.size() - 1]
        else:
            return None

    def first(self) -> Optional[T]:
        if self.list:
            return self.list[0]
        else:
            return None

    def size(self):
        return len(self.list)
