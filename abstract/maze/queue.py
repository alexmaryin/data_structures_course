from collections import deque
from typing import Generic, TypeVar

T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self):
        self._data = deque()

    @property
    def is_empty(self):
        return not self._data

    def push(self, item: T):
        self._data.append(item)

    def pop(self) -> T:
        return self._data.popleft()

    def __repr__(self):
        return repr(self._data)

