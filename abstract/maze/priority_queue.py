from heapq import heappush, heappop
from typing import Generic, TypeVar, List

T = TypeVar('T')


class PriorityQueue(Generic[T]):
    def __init__(self):
        self._data: List[T] = []

    @property
    def is_empty(self):
        return not self._data

    def push(self, item):
        heappush(self._data, item)

    def pop(self) -> T:
        return heappop(self._data)

    def __repr__(self):
        return repr(self._data)
