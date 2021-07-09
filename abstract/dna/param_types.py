from typing import TypeVar, Iterable, Protocol, Sequence

T = TypeVar('T')
C = TypeVar('C', bound='Comparable')


class Comparable(Protocol):
    def __eq__(self, other):
        return self == other

    def __lt__(self, other):
        return self < other

    def __gt__(self, other):
        return (not self < other) and self != other

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return not self < other


def linear_search(iterable: Iterable[T], key: T) -> int:
    for idx, item in enumerate(iterable):
        if item == key:
            return idx
    return -1


def binary_search(sequence: Sequence[C], key: C) -> int:
    low, high = 0, len(sequence) - 1
    while low <= high:
        mid = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            bound = mid
            while sequence[bound] == sequence[mid]: bound -= 1
            return bound + 1
    return -1
